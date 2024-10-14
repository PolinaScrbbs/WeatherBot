from dotenv import load_dotenv
import os

os.environ.pop("BOT_TOKEN", None)

os.environ.pop("API_URL", None)
os.environ.pop("API_KEY", None)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")