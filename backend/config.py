import os
from dotenv import load_dotenv

load_dotenv()

AZURE_API_KEY = os.getenv("API_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_API_VERSION = os.getenv("API_VERSION")
AZURE_DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_ID")
