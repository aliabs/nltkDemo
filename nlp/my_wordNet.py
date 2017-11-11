from nltk.corpus import wordnet

syns = wordnet.synsets("program")

print(syns[0].name)
