import requests
from bs4 import BeautifulSoup

def get_soup(url):
	rsp = requests.get(url)
	if rsp.status_code == 200:
		html = rsp.text
	soup = BeautifulSoup(html, 'lxml')
	return soup

def generate_article_info(soup):
	article_list = soup_today_articles.find_all('article', class_='rundown-segment')
	article_info = []
	for item in article_list:
		article = dict()
		article['title'] = item.find('h3').find('a').string
		article['catagory'] = item.find('h4').find('a').string
		article['mp3_src'] = item.find('li', class_='audio-tool audio-tool-download').find('a').get('href')
		article['duration'] = item.find('b', class_='audio-module-listen-duration').find_all('span')[1].string
		article_info.append(article)
	return article_info


archive_url = 'https://www.npr.org/programs/all-things-considered/archive'
soup_today_entry = get_soup(archive_url)
today_article_entry_url = soup_today_entry.find(class_="program-show__title").find('a').get('href')

soup_today_articles = get_soup(today_article_entry_url)
article_info_list = generate_article_info(soup_today_articles)
for each in article_info_list:
	print(each['title'])
	print('\t'+each['duration'])
	print('\t'+each['catagory'])
	print('\t'+each['mp3_src'])
	print('\n')


