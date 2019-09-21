import wikipedia as wiki

print(wiki.summary("Barack Obama"))


def _wikisearch(query):
    results = wiki.search(query, results=4)
    return results

def get_page_from_list(query_list, option_selected):
    selected = query_list[option_selected]
    return wiki.summary()
    
