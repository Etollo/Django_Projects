# from bs4 import BeautifulSoup
# import requests
# import MySQLdb
#
# db = MySQLdb.connect(host="localhost", user="root", passwd="00000000", db="db_django_project", charset='utf8')
# news = requests.get('http://izhlife.ru/news/')
#
# text = news.text
# soup = BeautifulSoup(text, 'html.parser')
# only_news = soup.find(id="il_all_news")
# news_a = only_news.find_all('h3')
# news = []
#
# cursor = db.cursor()
# for text in news_a:
#     news.append(text.get_text())
#
# for i in news:
#     sql = """INSERT INTO blog_news(News)
#             VALUES ('%(News)s')
#             """ % {"News": i}
#     cursor.execute(sql)
#     print("Done")
# db.commit()
