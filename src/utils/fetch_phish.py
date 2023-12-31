import requests
import json
import os
from dotenv import load_dotenv
from typing import List

load_dotenv()

def phish_tank_fetch_phishing_data() -> List | None:
    phish_tank_url = os.getenv("phish_tank_url")
    response = requests.get(phish_tank_url)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        return None