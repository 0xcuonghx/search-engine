import requests
import pandas
from bs4 import BeautifulSoup
import re
import const
from pyvi import ViTokenizer

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

def clean_data (content):
    list_words = ViTokenizer.tokenize(content).split()
    # Get stopword
    stopwords = []
    f = open('stopwords.txt', 'r', encoding="utf-8")
    for word in f:
        stopwords.append(word.strip())
    f.close()    
    words = [] # word after remove stop word
    for word in list_words:
        if word not in stopwords:
            words.append(word)
    return ' '.join(words)

def check_url_already_exist (url):
    f = open('url_exist.txt', 'a+')
    url_exist = []
    for o in f:
        url_exist.append(o)

    if url not in url_exist:
        f.write(url)
        f.write("\n")
        f.close()
        return False
    f.close()
    return True

def get_articles (url):
    soup = get_source_from(url)
    nodes = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5'], {"class": "title-news"})
    # next page ->>> 
    articles = []
    for node in nodes:
        a = node.find("a")
        href = a.get("href")
        if ( not check_url_already_exist(href)):
            title = a.get("title")
            content = get_article_content(href)
            content_clean = clean_data(content)
            articles.append([title, href, content, content_clean])    
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
    
    return pandas.DataFrame(articles, columns=['title', 'url', 'content', 'content_clean'])
