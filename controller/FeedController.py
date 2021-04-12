#!/usr/bin/python

import feedparser

class FeedController:

    def __init__(self, init_link):

        self.feed = feedparser.parse(init_link)["entries"]
    
    def get_feed_list(self):

        return self.feed

if __name__ == "__main__":

    test_link = "https://ekstrabladet.dk/rssfeed/all/"

    feed_list = FeedReader(test_link).get_feed_list()

    for one_feed in feed_list:

        print("%s | %s\n" % (one_feed["published"], one_feed["link"]))


    print("Ok")