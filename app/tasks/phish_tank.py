from app.models.phish import PhishData as PhishDataModel
from app.database import get_db
from sqlalchemy import exc
from app.utils.fetch_phish import phish_tank_fetch_phishing_data

def getPhish():

    # Verileri al
    phishing_data = phish_tank_fetch_phishing_data()
    # print(phishing_data[0])

    db = next(get_db())

    # Verileri kullanma örneği
    if phishing_data is not None:
        for entry in phishing_data:
            phish_id = entry['phish_id']
            url = entry['url']
            verified = entry['verified']
            online = entry['online']
            submission_time = entry['submission_time']
            verification_time = entry['verification_time']
            # İşlemleri burada yapabilirsiniz

            db_phish_data = PhishDataModel(phish_id=phish_id,
                                   url=url,
                                   verified=verified,
                                   online=online,
                                   submission_time=submission_time,
                                   verification_time=verification_time)
                
            try:
            # Yeni veriyi veritabanına kaydetme işlemi
                db.add(db_phish_data)
                db.commit()
                db.refresh(db_phish_data)
            except exc.IntegrityError as e:
            # Hata alındığında işlemleri geri al
                db.rollback()
    else:
        print("Phishing verileri alınamadı.")