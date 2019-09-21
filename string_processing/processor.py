import wikipedia as wiki
import nltk
import re
import functools
from gensim.summarization import summarizer

def _wiki_summary_filter(summary):
    braces_filtered = re.sub(r'\{.*\}', ' ', summary)
    return re.sub(r'[^\S]{2,}', ' ', braces_filtered)

def _wikisearch(query):
    results = wiki.search(query, results=4)
    return tuple(results)

def _get_page_from_list(query_list, option_index):
    selected = query_list[option_index]
    summary = wiki.summary(selected)
    return _wiki_summary_filter(summary)
    
def _summarize_data(full_string):
    condensed = summarizer.summarize(full_string)
    return condensed

def test(string):
    query_list = _wikisearch(string)
    page_sum = _get_page_from_list(query_list, 0)
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

@functools.lru_cache(maxsize=128)
def get_page_summary(query_list, option_index):
    """
    Paramaters -
        query_list: a non-empty list of query results
        option_index: an index for query_list from 0 to query_list length - 1
    Returns a string of summarized content, which should be split into an array of 
    text of 200-220 length
    """
    wiki_sum = _get_page_from_list(query_list, option_index)
    if(len(wiki_sum) <= 600):
        return wiki_sum
    else:
        return wiki_sum[:600]