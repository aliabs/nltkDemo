import math


def run(query, index):
    # calculate the IDF
    idf = {}
    query_vector = {}
    freq = {}
    for term in index:
        count_files = len(index)
        count_term_in_files = len(index[term])
        idf[term] = math.log10(count_files / count_term_in_files)
    # calculate the TF and the TF*IDF
    for term in query:
        freq[term] = query.count(term)
    max_value = max(freq.values())
    for term in query:
        query_vector[term] = (0.5 + 0.5*freq[term] / max_value) * idf.get(term, 0)
    return query_vector
