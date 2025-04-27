import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
      
# Bot Information
API_ID = int(environ.get("API_ID", "22977776"))
API_HASH = environ.get("API_HASH", "2ac7223d720bdeec757cbc88ced57224")
BOT_TOKEN = environ.get("BOT_TOKEN", "8096293701:AAHV35z-UT8X8AsjxBCdINyVfjJh90JT-SU")

PICS = (environ.get('PICS', 'https://envs.sh/yx6.jpg https://envs.sh/yxy.jpg https://envs.sh/yxX.jpg https://envs.sh/yxM.jpg https://envs.sh/yxm.jpg https://envs.sh/yxO.jpg https://envs.sh/yxa.jpg https://envs.sh/yxf.jpg https://envs.sh/yxg.jpg https://envs.sh/yxH.jpg')).split() # Bot Start Picture
FORCESUB_IMG = environ.get('FORCESUB_IMG', 'https://envs.sh/qny.jpg')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1397269319 1572929036 6762558871').split()]
AUTH_CHANNEL = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('AUTH_CHANNEL', '-1002680681271').split()] # give channel id with seperate space. Ex : ('-10073828 -102782829 -1007282828')
BOT_USERNAME = environ.get("BOT_USERNAME", "HTxFileStoreBot") # without @
PORT = environ.get("PORT", "8080")

# Database Information
DB_URI = environ.get("DB_URI", "mongodb+srv://jeevanantham8157:1055221@htxfilestorebot.3umybhw.mongodb.net/?retryWrites=true&w=majority&appName=HTxFileStoreBot")
DB_NAME = environ.get("DB_NAME", "HTxFileStoreBot")

# Clone Info :-
CLONE_MODE = bool(environ.get('CLONE_MODE', False)) # Set True or False

# If Clone Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
CLONE_DB_URI = environ.get("CLONE_DB_URI", "")
CDB_NAME = environ.get("CDB_NAME", "clonetechvj")

# Auto Delete Information
AUTO_DELETE_MODE = bool(environ.get('AUTO_DELETE_MODE', True)) # Set True or False

# If Auto Delete Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
AUTO_DELETE = int(environ.get("AUTO_DELETE", "30")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "600")) # Time in Seconds

# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002303784930"))

# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable - True or Disable - False
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# Verify Info :-
VERIFY_MODE = bool(environ.get('VERIFY_MODE', False)) # Set True or False

# If Verify Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
SHORTLINK_URL = environ.get("SHORTLINK_URL", "") # shortlink domain without https://
SHORTLINK_API = environ.get("SHORTLINK_API", "") # shortlink api
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "") # how to open link 

# Website Info:
WEBSITE_URL_MODE = bool(environ.get('WEBSITE_URL_MODE', False)) # Set True or False

# If Website Url Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
WEBSITE_URL = environ.get("WEBSITE_URL", "https://dailypostups.blogspot.com/2025/02/redirecting-to-your-link-code-credit.html") # For More Information Check Video On Yt - @Tech_VJ

# File Stream Config
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or False

# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://filestoresot.koyeb.app/")

#---------------------------------------------------------------------------------------------

#Set True Or Fales
LONG_IMDB_DESCRIPTION = bool(environ.get("LONG_IMDB_DESCRIPTION", False))
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)

# This Is File Channel Where You Upload Your File Then Bot Automatically Save It In Database 
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002266219670').split()]

#Newfeatures vars developer - @HeartThieft

DIRECT_GEN_DB = int(os.environ.get("DIRECT_GEN_DB", "-1002303784930"))
DIRECT_GEN_URL = os.environ.get("DIRECT_GEN_URL", "https://filestoresot.koyeb.app/")
DIRECT_GEN = bool(DIRECT_GEN_DB and DIRECT_GEN_URL)

POST_MODE= bool(environ.get('POST_MODE', True))
POST_SHORT_API = environ.get('POST_SHORT_API', '')
POST_SHORT_URL = environ.get('POST_SHORT_URL', '')

HOW_TO_POST_SHORT = environ.get('HOW_TO_POST_SHORT', 'https://t.me/Howtodowloa/13')

