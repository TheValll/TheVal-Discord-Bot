import os
from datetime import datetime
from dotenv import load_dotenv

class Utils:

    def get_date(formatted):
        date_today = datetime.now()
        if formatted == True:
            return date_today.strftime("%d/%m")
        else:
            return date_today
        
    def get_token():
        load_dotenv()
        return os.getenv("DISCORD_TOKEN")