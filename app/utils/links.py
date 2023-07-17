import os
from dotenv import load_dotenv

def getLinks():
    load_dotenv()

    PhishTank = os.getenv("PhishTank")
    j=0
    links = []
    while(j<10):
        links.append(PhishTank+f"{j}")
        j += 1

    return links