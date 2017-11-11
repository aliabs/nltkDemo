import glob
import os

from User import User


# 'D:\CSTI\Social Data Analysis\Project\dataset_twitter\dataset'

def run(path):
    users = {}
    counter = 0
    print('Indexing Files: START')
    for file in glob.glob(os.path.join(path, '*')):  # do your stuff
        iid = screen_name = description = location = url = lang = ''
        tweets_index = 0
        counter += 1
        if counter % 1000 == 0:
            print(str(counter))
            break
        with open(file, 'r', encoding="utf8") as myfile:
            data = myfile.readlines()
            for index, line in enumerate(data):
                key_value = line.split(':', 1)
                if key_value[0] == 'TweetId':
                    tweets_index = index
                    break
                if key_value[0] == 'ID':
                    iid = key_value[1]
                    continue
                if key_value[0] == 'Screen-name':
                    screen_name = key_value[1]
                    continue
                if key_value[0] == 'Description':
                    description = key_value[1]
                    # key_value = data[index + 1].split(':', 1)
                    # while key_value[0] != 'Location':
                    #     description += ' ' + key_value[0]
                    #     key_value = data[index + 1].split(':', 1)
                    continue
                if key_value[0] == 'Location':
                    location = key_value[1]
                    continue
                if key_value[0] == 'URL':
                    url = key_value[1]
                    continue
                if key_value[0] == 'Lang':
                    lang = key_value[1]
                    continue
            user = User(iid, screen_name, description, location, url, lang)
            for tweet in data[tweets_index + 1:]:
                if tweet.startswith('TweetId'):
                    continue
                user.add_tweet(tweet)
            users[iid] = user
    # words = ''
    # for user in users:
    #     words = users[user].words
    #     print(words)
    print('Indexing Files: END (' + str(counter) + ' indexed)')
    return users
