from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from ..models.phish import PhishData as PhishDataModel
from ..database import get_db
from sqlalchemy import exc
from ..utils.links import getLinks

def getPhish():
    
    urls = getLinks()

    chrome_options = Options()
    chrome_options.add_argument("--headless")


    driver = webdriver.Chrome(options=chrome_options)

    db = next(get_db())

    i=0
    while(i<len(urls)):

        driver.get(urls[i])
        content = driver.page_source
        time.sleep(3)
        soup = BeautifulSoup(content, 'html.parser')
        table = soup.find("table", class_="data")
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td", class_="value")
            if cells:
                phish_id = cells[0].find("a").text
                phish_url = cells[1].text
                submitted = cells[2].text.strip().replace("by ", "")
                valid = cells[3].text.strip()
                online = cells[4].text.strip()

                # print("ID:", phish_id)
                # print("Phish URL:", phish_url)
                # print("Submitted:", submitted)
                # print("Valid?:", valid)
                # print("Online?:", online)

                db_phish_data = PhishDataModel(
                                   identifier=phish_id,
                                   phish_url=phish_url,
                                   submitted_by=submitted,
                                   is_valid=valid,
                                   is_online=online)
                
                try:
                # Yeni veriyi veritabanına kaydetme işlemi
                    db.add(db_phish_data)
                    db.commit()
                    db.refresh(db_phish_data)
                except exc.IntegrityError as e:
                # Hata alındığında işlemleri geri al
                    db.rollback()
                

        del rows
        del table

        


        i+=1

    driver.quit()

    #time.sleep(10)