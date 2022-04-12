import wikipedia

def wikisearch(query):
    resp = wikipedia.search(query)
    return resp


def matchsearch(query):
    resp = wikipedia.page(query).summary
    return resp