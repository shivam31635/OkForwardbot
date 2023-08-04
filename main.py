#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os
from config import Config
from pyrogram import Client as ACE , idle
import asyncio, logging
import tgcrypto
from pyromod import listen
from logging.handlers import RotatingFileHandler

LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "log.txt", maxBytes=5000000, backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

# Auth Users
BOT_OWNER_ID = [ int(chat) for chat in Config.BOT_OWNER_ID.split(",") if chat != '']

# Prefixes 
prefixes = ["/", "~", "?", "!"]

plugins = dict(root="plugins")
if __name__ == "__main__" :
    AceBot = ACE(
        "AceBot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=120,
        plugins=plugins
    )
    
    async def main():
        await AceBot.start()
        bot_info  = await AceBot.get_me()
        LOGGER.info(f"<--- @{bot_info.username} Started (c) ACE --->")
        await idle()
    
    asyncio.get_event_loop().run_until_complete(main())
    LOGGER.info(f"<---Bot Stopped-->")
