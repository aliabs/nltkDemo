# *Screen-name: mjlambie
# Name: michael j lambie
# *Description: Head of Product @ https://t.co/eIJTow9Oa3
# Associate @ dontstealthismorningshow
# Husband / Father / Pet Owner
# *Location: Los Angeles, CA
# *URL: https://t.co/2k2ukfsg5g
# CreatedAt: Mon Jul 17 21:19:05 EEST 2006
# FollowersCount: 2837
# FriendsCount: 1149
# Lang: en
# TweetId: 725478935941640193	CreatedAt: Thu Apr 28 03:17:11 EEST 2016	Lang: en	Source: <a href="http://instagram.com" rel="nofollow">Instagram</a>	RetweetCount: 0
# Brass tax @ Jackson Square https://t.co/83HAiVm62d
from PreProcessing import DictionaryGenerator, DictionaryInvertedIndex, InputQuery, IndexingFiles, SimilarityMatch
from VSM import DocumentRepresentation, QueryRepresentation, DocumentRetrieval

path = 'D:\CSTI\Social Data Analysis\Project\dataset_twitter\dataset'
files = IndexingFiles.run(path)  # read the files and parse them, save data in structure makes latter processing easier
dictionary = DictionaryGenerator.run(files)  # from the files generate the dictionary using nltk
index = DictionaryInvertedIndex.run(dictionary, files)  # generate index, each word points to its source files
term_vector = DocumentRepresentation.run(files, index)  # apply the TF-IDF on each file and generate the vector
query = InputQuery.run()  # get user query and process it
query_files = SimilarityMatch.run(index, query)  # list of the files that contain the terms
query_vector = QueryRepresentation.run(query, index)  #
# select from the term vector the files from query files
matched_docs = DocumentRetrieval.run(term_vector, query_vector)  # apply cosine similarity
