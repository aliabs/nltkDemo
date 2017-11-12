from nltk.stem.wordnet import WordNetLemmatizer

lmtzr = WordNetLemmatizer()
print(lmtzr.lemmatize('cars'))
print(lmtzr.lemmatize('feet'))
print(lmtzr.lemmatize('people'))
print(lmtzr.lemmatize('fantasized','v'))
