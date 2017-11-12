from Tools.scripts.treesync import raw_input
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer


def run():
    stop_words = set(stopwords.words('english'))
    lmtzr = WordNetLemmatizer()
    query = raw_input('Enter your query:')
    query_tokenize = word_tokenize(query)
    query_filtered = []
    for w in query_tokenize:
        # and not re.match("^[a-zA-Z0-9]*$", w)
        if w not in stop_words and len(w) > 1:
            word_lemm = lmtzr.lemmatize(w)
            query_filtered.append(word_lemm)
    return query_filtered
