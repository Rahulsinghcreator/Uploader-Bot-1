import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess
import threading  # Import the threading module

import core as helper
#from utils import progress_bar
#from vars import API_ID as api_id
#from vars import API_HASH as api_hash
from vars import BOT_TOKEN as bot_token
#from vars import OWNER_ID as owner
#from vars import SUDO_USERS as sudo_users

from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = Client(
    name=":memory:",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token,
)

SUDOERS = filters.user()

#for x in sudo_users:
#    SUDOERS.add(int(x))
#if owner not in SUDOERS:
#    SUDOERS.add(int(owner))

# Define a function to handle the download task
async def download_task(bot, m, url, name, raw_text2, raw_text0, raw_text3, thumb):
    # Your download logic here...

@bot.on_message(filters.command(["dex"]) & SUDOERS)
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text('Send TXT file 📥')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await bot.send_document(-1002128896092, x)
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split("://", 1))
        os.remove(x)
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    # Create a list to store threads
    threads = []

    try:
        for i in range(count - 1, len(links)):
            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","")
            url = "https://" + V

            # Start a new thread for each download task
            thread = threading.Thread(target=download_task, args=(bot, m, url, name, raw_text2, raw_text0, raw_text3, thumb))
            thread.start()
            threads.append(thread)

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

    except Exception as e:
        await m.reply_text(e)

    await m.reply_text("🔰Done🔰")

bot.run()