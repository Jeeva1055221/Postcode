import os
import re
import logging
import imdb
from motor.motor_asyncio import AsyncIOMotorClient
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🔧 Bot Configurations
API_ID = int(os.getenv("API_ID", "16023154"))
API_HASH = os.getenv("API_HASH", "c216393ab439dd055858680916a3444b")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7203842216:AAHZx2eo9rSQiyW0BBcyZU72Tbzg887x3bc")
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://wemedia360:CuF1r3VUPJkYpZ7k@file2linkcaptoingen.fie8o.mongodb.net/?retryWrites=true&w=majority&appName=File2Linkcaptoingen")
TARGET_CHANNEL = int(os.getenv("TARGET_CHANNEL", "-1001842318978"))
ADMIN_ID = int(os.getenv("ADMIN_ID", "1397269319"))
BOT_USERNAME = os.getenv("BOT_USERNAME", "StoreFilesGetBot")

# 📂 MongoDB Setup
db_client = AsyncIOMotorClient(MONGO_URI)
db = db_client["telegram_bot"]
files_collection = db["files"]
config_collection = db["config"]

# 🎥 IMDb Setup
imdb_api = imdb.IMDb()

# 🔍 Get Caption Format
async def get_caption_format():
    config = await config_collection.find_one({"_id": "caption_format"})
    return config["format"] if config else "🎬 **Title:** {title}\n📅 **Year:** {year}\n⭐ **IMDb:** [{imdb_link}]({imdb_link})"

# 🎥 Fetch IMDb Poster & Info
async def get_poster(query):
    query = query.strip().lower()
    year_match = re.search(r'[1-2]\d{3}$', query)
    year = year_match.group() if year_match else None
    title = query.replace(year, "").strip() if year else query
    
    movie_results = imdb_api.search_movie(title)
    if not movie_results:
        return None

    movie = movie_results[0]  # First result
    movie_id = movie.movieID
    movie_data = imdb_api.get_movie(movie_id)

    return {
        'title': movie_data.get('title'),
        'year': movie_data.get('year', "Unknown"),
        'poster': movie_data.get('full-size cover url'),
        'imdb_link': f'https://www.imdb.com/title/tt{movie_id}'
    }

# 📁 Save File to DB
async def save_file(file_data):
    await files_collection.insert_one(file_data)

# 📂 Get Files by Title
async def get_files(title):
    return await files_collection.find({"title": title}).to_list(length=20)

# 🤖 Pyrogram Bot
app = Client("AutoPostBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# 📌 Auto-Save and Post on File Upload
@app.on_message(filters.channel & (filters.document | filters.video))
async def auto_post(client, message):
    file_name = message.document.file_name if message.document else message.video.file_name
    if not file_name:
        return

    title = " ".join(file_name.split(".")[:-1])
    movie_data = await get_poster(title)

    poster_url = movie_data.get("poster") if movie_data else None
    imdb_link = movie_data.get("imdb_link") if movie_data else "N/A"
    year = movie_data.get("year") if movie_data else "Unknown"

    file_data = {
        "file_id": message.document.file_id if message.document else message.video.file_id,
        "file_name": file_name,
        "file_size": message.document.file_size if message.document else message.video.file_size,
        "title": title,
        "year": year
    }
    await save_file(file_data)

    caption_format = await get_caption_format()
    caption = caption_format.format(title=title, year=year, imdb_link=imdb_link)

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎥 Download", url=f"https://t.me/{BOT_USERNAME}?start={title}")]
    ])

    if poster_url:
        await client.send_photo(TARGET_CHANNEL, poster_url, caption=caption, reply_markup=buttons)
    else:
        await client.send_message(TARGET_CHANNEL, caption, reply_markup=buttons)

# 📥 Handle File Downloads in Bot
@app.on_message(filters.command("start") & filters.private)
async def send_download_links(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply("Welcome! Use a valid download link.")
        return

    search_title = args[1]
    files = await get_files(search_title)

    if not files:
        await message.reply("No files found for this title.")
        return

    reply_text = f"🎥 **Download Options for {search_title}:**\n"
    buttons = []

    for file in files:
        size_mb = round(file["file_size"] / (1024 * 1024), 2)
        file_id = file["file_id"]
        buttons.append([InlineKeyboardButton(f"{size_mb}MB", callback_data=f"download_{file_id}")])

    await message.reply(reply_text, reply_markup=InlineKeyboardMarkup(buttons))

# 📤 Send Selected File on Button Click
@app.on_callback_query(filters.regex(r"download_(.*)"))
async def send_selected_file(client, callback_query):
    file_id = callback_query.data.split("_")[1]
    await callback_query.message.reply_document(file_id)

# 🚀 Run Bot
app.run()
