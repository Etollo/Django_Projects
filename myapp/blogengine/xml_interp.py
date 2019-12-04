from bs4 import BeautifulSoup
from urllib.request import urlopen

page = urlopen('https://mkechinov.ru/offercategory.html')
soup = BeautifulSoup(page, 'html.parser')
option_tag = soup.new_tag('option')

for i in soup.find_all('strong'):
    print(i.get_text())

