#!/usr/bin/env python3
import os
from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", 12345))
    API_HASH = environ.get("API_HASH")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6079360237:AAH9vyBqhrZDl7vOqb1KzvqSaaMEL2hBA-Y") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://shivam41:shivam41@cluster0.x6odn7r.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "cluster0")
    BOT_OWNER_ID = os.environ.get("BOT_OWNER_ID", "25069425")

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
