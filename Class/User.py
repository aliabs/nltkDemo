

class User:
    def __init__(self, iid, screen_name, description, location, url, lang):
        self.iid = iid
        self.screen_name = screen_name
        self.description = description
        self.location = location
        self.url = url
        self.lang = lang
        self.tweets = []
        self.tags = []

    def add_tweet(self, tweet):
        self.tweets.append(tweet)

    @property
    def format(self):
        r = 'Id:  ' + self.iid + '\nScreen Name:  ' + self.screen_name + '\nDescription:  ' + self.description + '\nLocation:  ' + self.location + '\nURL:  ' + self.url + '\nLang:  ' + self.lang + '\nTweets: '
        for tweet in self.tweets:
            r += '\n    ' + tweet
        return r

    @property
    def words(self):
        r = self.iid + self.screen_name + self.description + self.location + self.url + self.lang
        for tweet in self.tweets:
            r += ' ' + tweet
        return r