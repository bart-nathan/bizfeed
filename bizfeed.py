#!/usr/bin/python

import feedparser
import os
import sys
from datetime import datetime

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

def convert_date(input_string):

    split_string = input_string.split(",")[1].split(" ")
    time_split = split_string[4].split(":")

    day = int(split_string[1])
    month =  int(found_month(split_string[2]))
    year = int(split_string[3])
    
    hours = int(time_split[0])
    minutes = int(time_split[1])
    seconds = int(time_split[2])

    return datetime(year,month, day, hours,minutes,seconds)

def convert_date_old(date_string):
    
    split_string = date_string.split(" ")
    build_string = "%s-%s-%s-%s" % (split_string[1], found_month(split_string[2]), split_string[3], split_string[4])
    return build_string

def is_today(date_string):
    
    now_date = str(datetime.now()).split(" ")[0].split("-")
    input_date = str(date_string).split(" ")[0].split("-")
    
    if (now_date[0] == input_date[0]) and (now_date[1] == input_date[1]) and (now_date[2] == input_date[2]):
        return True
     
    
    #print(now_date)
    #print(input_date)

    return False

def mix_feeds():

    found_feeds = []

    for one_feed in feed_list:

        item_list = feedparser.parse(one_feed[1])["entries"]

        for item in item_list:

            feed_date = convert_date(item["published"])
            
            if (is_today(feed_date)):

                found_feeds.append([feed_date,item["title"], item["link"], one_feed[0]])
    
    return sorted(found_feeds, reverse=False)

def show_feed_list(f_list):

    index = 0

    for f in f_list:

        count, date, title, link, feed_name = f 
        print("%s | %s | %s | %s" % (count,date,title,feed_name ))

def display_menu():

    #try:
        f_list = get_feeds()
    
        command = None

        show_feed_list(f_list)

        while command != 'q':

            print("? for help :>", end='')
            command = input()

            if command == "list":

                show_feed_list(f_list)
            
            elif command.split(" ")[0] == "read":

                number = int(command.split(" ")[1])

                os.system("links %s" % (f_list[number - 1][3]))
                #print("number is %s" % number)
            
            elif command == "?":

                print("list     :   get the feedlist")
                print("read     :   read a feed")
                print("q        :   quit the program")
        
    #except Exception as ex:
        
     #   print(ex)
        
if __name__ == "__main__":

    #result = is_today("2021-04-18")

    #print(result)
    
    display_menu()
    #print(datetime.now())