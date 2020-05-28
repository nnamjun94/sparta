import requests
from bs4 import BeautifulSoup



# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
# 전체 테이블 
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1)
# 순위
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number > span
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number > span > span
# 제목
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
# 가수
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
music_list = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in music_list:
    a_tag = music.select_one('td.info > a.title.ellipsis')
    if a_tag is not None:
        title = a_tag.text
        rank = music.select_one('td.number').text
        rank_1 = music.select_one('td.number > span').text
        rank_2 = rank.replace(rank_1,"")
        singer = music.select_one('td.info > a.artist.ellipsis').text

        print(rank_2.strip(), title.strip(), singer)