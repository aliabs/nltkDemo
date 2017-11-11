
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))
example_sentence = "Hello World, From Mr. Python. NLTK is simple!"

words = word_tokenize(example_sentence)

filtered_sentence = []

# for w in words:
#     if w not in stop_words:
#         filtered_sentence.append(w)
filtered_sentence = [w for w in words if not w in stop_words]
print(filtered_sentence)