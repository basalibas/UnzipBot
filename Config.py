import os


class Config:
    API_ID = int(os.environ.get("1893177", 0))  # Change 12345 to your API_ID
    API_HASH = os.environ.get("84ce113c503f77e04fcaacc1c0d040f0", None)  # Change None to your API_HASH
    BOT_TOKEN = os.environ.get("1802568819:AAGjYC8neFZazxn8zIVMdd-iplx20c-7krA", None)  # Change None to your BOT_TOKEN
    OWNER_ID = int(os.environ.get("OWNER_ID", 0))  # Change 0 to your OWNER_ID
    OWNER_NAME = os.environ.get("OWNER_NAME", None)  # Change None to your OWNER_NAME

    # For Local Deploys edit above 5 lines.
    # Put your API_ID and OWNER_ID (without comma) and API_HASH,BOT_TOKEN n OWNER_NAME (with commas) below.
    # If got any problem ask in @MysteryBotsChat.
