from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
def getBBCNews():
  news_url = "http://feeds.bbci.co.uk/news/rss.xml?edition=uk"
  Client=urlopen(news_url)
  xml_page=Client.read()
  Client.close()

  soup_page = soup(xml_page,"xml")
  news_list = soup_page.findAll("item")
  allNews = []
  for news in news_list:
    allNews.append(news.title.text)
    allNews.append(". ")
  return(allNews)