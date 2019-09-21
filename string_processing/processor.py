import wikipedia as wiki
import nltk
from gensim.summarization import summarizer

def _wikisearch(query):
    results = wiki.search(query, results=4)
    return results

def _get_page_from_list(query_list, option_index):
    selected = query_list[option_index]
    summary = wiki.summary(selected)
    return summary
    
def _summarize_data(full_string):
    condensed = summarizer.summarize(full_string)
    return condensed

def test(string):
    query_list = _wikisearch(string)
    page_sum = _get_page_from_list(query_list, 1)
    print("1.")
    print(page_sum, end="\n\n\n")
    cond = _summarize_data(page_sum)
    print("2.")
    print(cond)
    return cond

def get_query_list(search_string):
    """
    Returns the query list from wikipedia for a search string.
    """
    return _wikisearch(search_string)

def get_page_summary(query_list, option_index):
    wiki_sum = _get_page_from_list(query_list, option_index)
    if(len(wiki_sum) <= 600):
        return wiki_sum
    else:
        return _summarize_data(wiki_sum)

test("Stockfish")