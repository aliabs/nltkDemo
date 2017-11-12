from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer


def run(users):
    print('Generating Dictionary: START')
    stop_words = set(stopwords.words('english'))
    lmtzr = WordNetLemmatizer()
    counter = 0
    filtered_words = []

    for user in users:
        counter += 1
        if counter % 100 == 0:
            print(str(counter))
        text = users[user].words
        word_tokens = word_tokenize(text)
        for w in word_tokens:
            # and not re.match("^[a-zA-Z0-9]*$", w)
            if w not in stop_words and len(w) > 1:
                word_lemm = lmtzr.lemmatize(w)
                word_lemm = word_lemm.lower()
                users[user].tags.append(word_lemm)
                filtered_words.append(word_lemm)
        filtered_words.sort(key=str.lower)
    sorted_words = list(set(filtered_words))
    print('Generating Dictionary: END (' + str(len(sorted_words)) + ' term)')
    return sorted_words
