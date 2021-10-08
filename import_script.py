from app import db, Bitcoin
from scrape import scraper

url = "https://coinmarketcap.com/2/"
scraper_data = scraper(url)

def put_together():
    #will make sure the database empty
    db.drop_all()
    #create the columns of database
    db.create_all()
    #iterates via the table while scraping at the same time, and filling the coumns with the info
    #ממלא את העמודות עם המידע והשמות של העמודות
    for coin in scraper_data:
        new_row = Bitcoin(Name = coin[0], Price=coin[1], _24h=coin[2], _7d=coin[3], Market_Cap=coin[4], Volume=coin[5],Circulating_Supply=coin[6])
        db.session.add(new_row)
        db.session.commit()


if __name__ == '__main__':
    put_together()
