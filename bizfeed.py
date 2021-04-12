#!/usr/bin/python

import feedparser
import os
import sys


feed_list = []
feed_list.append(["Ekstrabladet", "https://ekstrabladet.dk/rssfeed/all/"] )
feed_list.append(["Dr Nyheder", "https://www.dr.dk/nyheder/service/feeds/allenyheder"] )
feed_list.append(["Nyborg", "https://fyens.dk/feed/nyborg"])
feed_list.append(["Computerworld", "https://www.computerworld.dk/rss/all"])

def found_month(init_month):
    
    months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug","Sept", "Oct", "Nov", "Dec"]
    count = 0
    for m in months:

        if m == init_month:
            return count + 1
        
        count = count + 1
    
    return 0

def get_feeds():
    found_feeds = []
    count = 0
    feeds = mix_feeds()

    for f in feeds:
        
        date, title, link, feed_name = f

        found_feeds.append([count, date,title,link,feed_name])

        count = count + 1

    return found_feeds


def mix_feeds():

    found_feeds = []

    for one_feed in feed_list:

        item_list = feedparser.parse(one_feed[1])["entries"]

        for item in item_list:



            found_feeds.append([item["published"],item["title"], item["link"], one_feed[0]])
            #print("%s | %s | %s" % (item["published"].split(" ")[4], item["title"], one_feed[0]))
    
    return sorted(found_feeds)

    #return feedparser.parse(test_link)["entries"]


def display_content():

     #try:

        command = sys.argv[1]

        if command == "read":
            print("read a feed")

        if command == "list":
            
            f_list = get_feeds()

            for f in f_list:

                count, date, title, link, feed_name = f 
                print(" %s | %s | %s | %s" % (count,date, title,feed_name))


    #except Exception as ex:
     #    print(ex)

if __name__ == "__main__":

    display_content()

    #print(found_month("July"))

    
   

