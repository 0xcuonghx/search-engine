import requests
import pandas
from bs4 import BeautifulSoup
import re
import const

def get_source_from(url):
    print("Requesting to {} ...".format(url))
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    return soup

def get_categorize(baseUrl):
    soup = get_source_from(baseUrl)
    menu = soup.find("ul", {"class": "parent"})
    href = menu.findAll("a")
    categorize = []
    for child in href:
        link = child.get("href")
        if re.match("^/\w+", link):
            categorize.append(baseUrl+link[1:])
    return categorize

def get_articles (url):
    soup = get_source_from(url)
    nodes = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5'], {"class": "title-news"})
    # next page ->>> 
    articles = []
    for node in nodes:
        a = node.find("a")
        href = a.get("href")
        title = a.get("title")
        content = get_article_content(href)
        articles.append([title, href, content])
    # return pandas.DataFrame(articles, columns=['title', 'url', 'content'])
    return articles

def get_article_content(url):
    soup = get_source_from(url)
    text_nodes = soup.find_all("p")
    content = ''
    for text in text_nodes:
        content += text.get_text()
    return content

def crawler () :
    categorize = get_categorize(const.baseUrl)
    articles = []
    for link in categorize:
        articles += get_articles(link)
    
    return pandas.DataFrame(articles, columns=['title', 'url', 'content'])
