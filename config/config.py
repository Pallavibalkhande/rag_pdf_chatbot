import os
from dotenv import load_dotenv
 
load_dotenv()
 
API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = "https://openai.generative.engine.capgemini.com/v1"