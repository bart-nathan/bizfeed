#!/usr/bin/python

import feedparser

class FeedReader:

    def __init__(self, init_link):

        self.feed = feedparser.parser(init_link)["entries"]
    
    def get_feed_list(self):

        feed_list = []

        return feed_list