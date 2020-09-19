import requests
from bs4 import BeautifulSoup


url = 'https://www.youtube.com/channel/UCuPNoEZUan3WybeJawo9gNQ'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
r = requests.get(url, headers=headers)
bs = BeautifulSoup(r.text, 'html.parser')
links = bs.find_all('a')
for link in links:
    print(link['href'])