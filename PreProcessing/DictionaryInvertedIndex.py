from collections import defaultdict


def run(dic_words, files):
    print('Indexing Dictionary with Files: START')
    counter = 0
    index = defaultdict(list)
    for word in dic_words:
        counter += 1
        if counter % 1000 == 0:
            print(str(counter))
        for file in files:
            if word in files[file].tags:
                index[word].append(file)
    print('Indexing Dictionary with Files: END  (', str(counter), ' term where indexed')
    return index
