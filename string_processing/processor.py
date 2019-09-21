import wikipedia as wiki
import nltk
from gensim.summarization import summarizer

def _wikisearch(query):
    results = wiki.search(query, results=4)
    return results

def _get_page_from_list(query_list, option_selected):
    selected = query_list[option_selected]
    summary = wiki.summary(selected)
    print("1.")
    print(summary, end="\n\n\n")
    return summary
    
def _summarize_data(full_string):
    condensed = summarizer.summarize(full_string)
    print("2.")
    print(condensed)
    return condensed

def test(string):
    query_list = _wikisearch(string)
    page_sum = _get_page_from_list(query_list, 1)
    return _summarize_data(page_sum)

test("Stockfish")