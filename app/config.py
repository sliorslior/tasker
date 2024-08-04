import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PORT = os.getenv('PORT', 3000)
    DEBUG = os.getenv('DEBUG', 'False') == 'True'