import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&SearchWord=%ED%98%B8%EB%B0%80%EB%B0%AD%EC%9D%98+%ED%8C%8C%EC%88%98%EA%BE%BC&x=0&y=0',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#Search3_Result > div:nth-child(1) > table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li:nth-child(4) > span.ss_p2 > b > span')
print(trs.text)

#@app.route('/book_info')
#def book_info_get():
 #   search_text = request.args.get('search_text')
  #  search_text = search_text.replace(" ", "+")
   # url = 'https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&SearchWord=' + search_text + '&x=0&y=0'
    #headers = {
      #  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
   # data = requests.get(url, headers=headers)

    #soup = BeautifulSoup(data.text, 'html.parser')

    #name = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info.character > h3 > a').text
    #img_url = soup.select_one('#content > div.article > div.mv_info_area > div.poster > img')['src']
    #recent = soup.select_one(
     #   '#content > div.article > div.mv_info_area > div.mv_info.character > dl > dd > a:nth-child(1)').text
