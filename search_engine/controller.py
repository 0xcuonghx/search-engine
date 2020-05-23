import pysolr
import json
from pyvi import ViTokenizer
import utils

SOLR_SERVER = 'http://localhost:8983/solr/IT4853'

def connect_solr():
    try:
        solr = pysolr.Solr(SOLR_SERVER, always_commit=True)
        solr.ping() # check solr alive
        print("Connection success!!")
        return solr
    except Exception:
        print("[ERROR] Connect_error: Something went wrong!")
        return

def search (query, page=1):
    try:
        solr = connect_solr()
        list_words = ViTokenizer.tokenize(query).split()
        stopwords = utils.get_stopwords()
        words = [] # word after remove stop word
        for word in list_words:
            if word not in stopwords:
                words.append(word)
        clean_query = ' '.join(words)
        results = solr.search("content_clean:{}".format(clean_query), **{'fl': '*, score', 'start': '{}'.format((page - 1)*10)})
        return { "results": results, "numFound": results.raw_response['response']['numFound']}
    except Exception:
        print("[ERROR] search error: Something went wrong!")


def search_synonym (query):
    try:
        solr = connect_solr()
        list_words = ViTokenizer.tokenize(query).split()
        stopwords = utils.get_stopwords()

        words = [] # word after remove stop word
        for word in list_words:
            if word not in stopwords:
                words.append(word)
        
        
    except Exception:
        print("[ERROR] search synoym error: Something went wrong!")


search("covid", 1)