from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def run(users):
    print('Generating Dictionary: START')
    stop_words = set(stopwords.words('english'))
    counter = 0
    filtered_sentence = []

    for user in users:
        counter += 1
        if counter % 100 == 0:
            print(str(counter))
        text = users[user].words
        word_tokens = word_tokenize(text)
        for w in word_tokens:
            # and not re.match("^[a-zA-Z0-9]*$", w)
            if w not in stop_words and len(w) > 1:
                users[user].tags.append(w)
                filtered_sentence.append(w)
    filtered_sentence.sort(key=str.lower)
    sort = list(set(filtered_sentence))
    print('Generating Dictionary: END (' + str(len(sort)) + ' term)')
