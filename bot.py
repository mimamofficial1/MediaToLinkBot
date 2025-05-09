from datetime import datetime
from pytz import timezone
from pyrogram import Client, __version__, filters
from pyrogram.raw.all import layer
from aiohttp import web
from utils import web_server
import os, time
from catbox import CatboxUploader
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# pyro client config
API_ID    = os.environ.get("API_ID", "23631217") # input api id
API_HASH  = os.environ.get("API_HASH", "567c6df308dc6901790309499f729d12") # input api hash
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8153208191:AAET_YAHGjeLFNXf0q1Wy1zWVoGNwcyMnlY") # input bot token

# other configs
BOT_UPTIME = time.time()
PORT = int(os.environ.get('PORT', '8080')) # input PORT
ADMIN = int(os.environ.get('ADMIN', '6139759254')) # input user id

class ImageToLinkBot(Client):
    def __init__(self):
        super().__init__(
            name="ImageToLinkBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={"root": "MediaToLinkBot"},
            workers=200,
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username  
        self.uptime = BOT_UPTIME
        
        app = web.AppRunner(await web_server())
        await app.setup()       
        await web.TCPSite(app, "0.0.0.0", PORT).start()
            
        print(f"{me.first_name} Started.....✨️")
        if ADMIN:
            try: await self.send_message(ADMIN, f"**__{me.first_name} Started.....✨️__**")                                
            except: pass
                
        
    async def stop(self, *args):
        await super().stop()
        print("Bot Stopped 🙄")

            
ImageToLinkBot().run()
#Rkn_AutoCaptionBot().run()
