#!/usr/bin/python

import feedparser

feed_list = []
feed_list.append(["nyheder", "https://ekstrabladet.dk/rssfeed/all/"] )
feed_list.append(["nyheder", "https://www.dr.dk/nyheder/service/feeds/allenyheder"] )



#test_link = "https://ekstrabladet.dk/rssfeed/all/"

def display_feeds():

    for one_feed in feed_list:

        item_list = feedparser.parse(one_feed[1])["entries"]

        for item in item_list:

             print("%s | %s\n" % (item["published"], item["link"]))

            
        

        print(one_feed)
    

    #return feedparser.parse(test_link)["entries"]



if __name__ == "__main__":

    display_feeds()

'''
    f_list = get_feeds()

    for one_feed in f_list:

        print("%s | %s\n" % (one_feed["published"], one_feed["link"]))

    print("ok")

'''
