
def get_stopwords ():
    stopwords = []
    f = open('stopwords.txt', 'r', encoding="utf-8")
    for word in f:
        stopwords.append(word.strip())
    f.close()
    return stopwords

def get_synonym_of(word):
    
    return ''

get_synonym_of("hoặc")