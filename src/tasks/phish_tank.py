import os
from dotenv import load_dotenv
load_dotenv()
PROJECT_PATH = os.getenv("PROJECT_PATH")
import sys
sys.path.append(PROJECT_PATH)

from src.models.phish import PhishData as PhishDataModel
from src.database import get_db
from sqlalchemy import exc
from src.utils.fetch_phish import phish_tank_fetch_phishing_data
from src.tasks.celery_config import celery_app, logger

@celery_app.task
def get_phish():

    phishing_data = phish_tank_fetch_phishing_data()

    db = next(get_db())

    if phishing_data is not None:
        for entry in phishing_data:
            phish_id = entry['phish_id']
            url = entry['url']
            verified = entry['verified']
            online = entry['online']
            submission_time = entry['submission_time']
            verification_time = entry['verification_time']

            db_phish_data = PhishDataModel(phish_id=phish_id,
                                   url=url,
                                   verified=verified,
                                   online=online,
                                   submission_time=submission_time,
                                   verification_time=verification_time)
                
            try:
                db.add(db_phish_data)
                db.commit()
                db.refresh(db_phish_data)
            except exc.IntegrityError as e:
                db.rollback()
    else:
        logger.info("Failed to retrieve phishing data.")