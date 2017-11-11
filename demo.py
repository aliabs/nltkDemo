import glob
import os
from nltk.tokenize import sent_tokenize, word_tokenize

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
import DictionaryGenerator
import IndexingFiles

path = 'D:\CSTI\Social Data Analysis\Project\dataset_twitter\dataset'
users = IndexingFiles.run(path)
DictionaryGenerator.run(users)

# words = ''
# for user in users:
#     words = users[user].words
#     print(words)