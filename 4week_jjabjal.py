import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

# rank td.number
# name td.info > a.title.ellipsis
# writer td.info > a.artist.ellipsis

for tr in trs:
    rank = tr.select_one('td.number').text[:2].strip()
    name = tr.select_one('td.info > a.title.ellipsis').text.strip()
    artist = tr.select_one('td.info > a.artist.ellipsis').text

    print(rank,name,artist)

    music = {
        'rank': rank,
        'name': name,
        'artist': artist
    }

    db.music.insert_one(music)

    