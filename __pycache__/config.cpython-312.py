# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: /app/config.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 2025-02-01 19:22:31 UTC (1738437751)

import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = 26741932
    API_HASH = "d9037cbe01f292eb440468c39c3dc41d"
    ADMIN_ID = [6793357832]
    DB_URL = "mongodb+srv://navedmohammad2516:zu02cmOW6medghcJ@cluster0.cq1x5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    DB_NAME = os.environ.get("DB_NAME")
    TXT_LOG = -1002322908140
    HOST = "https://www.masterapi.tech"
