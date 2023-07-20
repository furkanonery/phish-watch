from app.models.phish import PhishData as PhishDataModel
from app.database import get_db
from sqlalchemy import exc
from app.utils.fetch_phish import phish_tank_fetch_phishing_data

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
        print("Phishing verileri alınamadı.")