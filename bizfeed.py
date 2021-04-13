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
    count = 1
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

            found_feeds.append([convert_date(item["published"]),item["title"], item["link"], one_feed[0]])
    
    return sorted(found_feeds, reverse=True)

def show_feed_list(f_list):

    index = 0

    for f in f_list:

        count, date, title, link, feed_name = f 
        print("%s | %s | %s | %s" % (count,date,title,feed_name ))

        if index % 20 == 0:

            print(":>", end='')
        
            choise = input()

            if  choise != "":

                if (choise == "q"):

                    sys.exit()
                
                else:
                    os.system("links %s" % (f_list[int(choise) - 1][3]))

        index = index + 1

def display_menu():

    try:
        f_list = get_feeds()
    
        command = None

        show_feed_list(f_list)

        while command != 'q':

            print("? for help :>", end='')
            command = input()

            if command == "list":

                show_feed_list(f_list)
            
            elif command == "read":

                print("item number :", end='')

                number = int(input())

                os.system("links %s" % (f_list[number - 1][3]))
                #print("number is %s" % number)
            
            elif command == "?":

                print("list     :   get the feedlist")
                print("read     :   read a feed")
                print("q        :   quit the program")
        
    except Exception as ex:
        
        print(ex)
        
if __name__ == "__main__":

    display_menu()