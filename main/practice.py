from bs4 import BeautifulSoup
import requests

source = requests.get('https://coreyms.com/').text
#print(source)

soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

article = soup.find('article')

# print(article.prettify())

# headline = article.a.text #Headline of text
# print(headline)

# summary = article.find('div', class_='entry-content').p.text
# print(summary)

vid_src = article.find('iframe', class_='youtube-player')['src']
print(vid_src)