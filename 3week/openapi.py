import requests # requests 라이브러리 설치 필요
# requests.get(url)
# requests.post(url,data={"id":"username"})
r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()
#print (rjson['RealtimeCityAir']['row'][0]['NO2'])
#(상위 코드 : 중구의 NO2 값을 가져오고 싶을 때)
gus=rjson['RealtimeCityAir']['row']
for gu in gus:
    #print(gu['MSRSTE_NM'], gu['IDEX_MVL'])
    #(상위 코드 : 모든 미세먼지 IDEX_MVL 수치 보고 싶을 때)
    gu_name = gu["MSRRGN_NM"]
    misae_value = gu["IDEX_MVL"]
#print(gu_name + ' : ' + str(misae_value))
#str : 강제로 문자열로 변환시켜줌
#gu_name, : : 문자열
#(misae_value) : 숫자
    if misae_value < 100 :
        print(gu_name)
#(상위 코드 : 지수 100 미만 값 보고 싶을 때, 현재 활성화된 상태)

#웹스크래핑
import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#############################
# (입맛에 맞게 코딩)
#############################

movies = soup.select('#old_content > table > tbody > tr')
rank=1
for movie in movies:
    # movie는 개발자가 임의로 만드는 단어
    # movie 안에 a 가 있으면,
    a_tag = movie.select_one('td.title > div > a')
    point = movie.select_one('td.point')
    #태그가 td면서, 동시에 class가 point이라는 의미
    if a_tag is not None:
        # a의 text를 찍어본다.
        print (rank, a_tag.text, point.text)
        rank=rank+1


