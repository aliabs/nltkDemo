import math


def run(files, index):
    term_vector = {}
    idf = {}
    # calculate the IDF
    for term in index:
        count_files = len(index)
        count_term_in_files = len(index[term])
        idf[term] = math.log10(count_files / count_term_in_files)
    # calculate the TF and the TF*IDF
    for file in files:
        freq = {}
        term_weight = {}
        for term in index:
            freq[term] = files[file].tags.count(term)
        max_value = max(freq.values())
        for term in freq:
            term_weight[term] = (freq[term] / max_value) * idf.get(term, 0)
        term_vector[file] = term_weight
    return term_vector
