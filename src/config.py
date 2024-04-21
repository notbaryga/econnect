import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")
AUTH_SECRET = os.environ.get("AUTH_SECRET")
