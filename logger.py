
#Project me aane wale errors ko file me save karna.
from datetime import datetime

LOG_FILE = "logs/error.log"

def log_error(file_name, error_message):

    with open(LOG_FILE, "a") as file:   #Append mode=purane errors delete nahi karte

        file.write(
            f"[{datetime.now()}] "
            f"{file_name} -> {error_message}\n"
        )
