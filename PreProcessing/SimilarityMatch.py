
def run(index, query):
    # query_files = {}
    # for term, file in index.items():
    #     print(term)
    #     if str(term) in query:
    #         query_files[term] = file
    query_files = dict((k, v) for k, v in index.items() if k in query)
    return query_files
