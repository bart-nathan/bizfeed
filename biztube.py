#!/usr/bin/python

import feedparser
import os
import sys
from datetime import date

feed_list = []
feed_list.append(["Explaining Computers", "https://www.youtube.com/feeds/videos.xml?user=explainingcomputers"])

def found_month(init_month):
    
    months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug","Sept", "Oct", "Nov", "Dec"]
    count = 0
    for m in months:

        if m == init_month:
            
            if count < 10:
                return "%s%s" % ("0",count + 1)
            
            else:
                return count + 1
        
        count = count + 1
    
    return 0


def mix_feeds():

    found_feeds = []

    for one_feed in feed_list:

        item_list = feedparser.parse(one_feed[1])["entries"]
        
        for item in item_list:

            found_feeds.append([item["published"],item["title"], item["link"], one_feed[0]])
    
    return sorted(found_feeds, reverse=True)
    

if __name__ == "__main__":

    mix_feeds()
