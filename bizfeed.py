#!/usr/bin/python

import feedparser
import os
import sys
from datetime import date


feed_list = []
feed_list.append(["Ekstrabladet", "https://ekstrabladet.dk/rssfeed/all/"] )
feed_list.append(["Dr Nyheder", "https://www.dr.dk/nyheder/service/feeds/allenyheder"] )
feed_list.append(["Nyborg", "https://fyens.dk/feed/nyborg"])
feed_list.append(["BBC Europe", "http://feeds.bbci.co.uk/news/world/europe/rss.xml"])
feed_list.append(["BT", "https://www.bt.dk/bt/seneste/rss"])
#feed_list.append(["Version2", "https://www.version2.dk/it-nyheder/rss"])

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

def get_feeds():
    found_feeds = []
    count = 0
    feeds = mix_feeds()

    for f in feeds:
        
        date, title, link, feed_name = f

        found_feeds.append([count, date,title,link,feed_name])

        count = count + 1

    return found_feeds


def convert_date(date_string):
    
    split_string = date_string.split(" ")
    
    build_string = "%s-%s-%s-%s" % (split_string[1], found_month(split_string[2]), split_string[3], split_string[4])

    return build_string


def mix_feeds():

    found_feeds = []

    for one_feed in feed_list:

        item_list = feedparser.parse(one_feed[1])["entries"]

        for item in item_list:

            feed_date = convert_date(item["published"]).split("-")
            current_date = date.today().strftime("%d-%m-%Y").split("-")

            if (feed_date[0] == current_date[0]) and (feed_date[1] == current_date[1] ):

                found_feeds.append([convert_date(item["published"]),item["title"], item["link"], one_feed[0]])
            #print("%s | %s | %s" % (item["published"].split(" ")[4], item["title"], one_feed[0]))
    
    #return found_month.sort(reverse=False)
    return sorted(found_feeds, reverse=True)

    #return feedparser.parse(test_link)["entries"]


def display_content():

    try:

        command = sys.argv[1]
        f_list = get_feeds()

        if command == "read":
            
            number = int(sys.argv[2])
            os.system("links %s" % (f_list[number][3]))
           
        if command == "list":

            for f in f_list:

                count, date, title, link, feed_name = f 
                print("%s | %s | %s | %s" % (count,date,title,feed_name ))
                
    except Exception as ex:
        
        print(ex)

if __name__ == "__main__":

    display_content()

    #print(found_month("July"))

    
   

