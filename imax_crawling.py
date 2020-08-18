import requests
from bs4 import BeautifulSoup


def job_function():
    url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200826'
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    title_list = soup.select('div.info-movie')
    imax = soup.select_one('span.imax')
    if imax:
        imax = imax.find_parent('div', class_='col-times')
        title = imax.select_one('div.info-movie > a >strong').text.strip()
        return title
    else:
        return None