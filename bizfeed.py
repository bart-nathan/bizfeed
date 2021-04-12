#!/usr/bin/python

import feedparser

test_link = "https://ekstrabladet.dk/rssfeed/all/"

def get_feeds():

    return feedparser.parse(test_link)["entries"]



if __name__ == "__main__":


    f_list = get_feeds()

    for one_feed in f_list:

        print("%s | %s\n" % (one_feed["published"], one_feed["link"]))

    print("ok")
