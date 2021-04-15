#!/usr/bin/python

import feedparser
import os
import sys
from datetime import datetime

feed_list = []
feed_list.append(["Explaining Computers", "https://www.youtube.com/feeds/videos.xml?user=explainingcomputers"])
feed_list.append(["Udstødt", "https://www.youtube.com/feeds/videos.xml?channel_id=UCfuFrEavX-B7FIcC5geJUpg"])
feed_list.append(["Peters Plader","https://www.youtube.com/feeds/videos.xml?channel_id=UCp_abvqvoCyWgLrXaOEHEEA"])
feed_list.append(["The Hated One","https://www.youtube.com/feeds/videos.xml?channel_id=UCjr2bPAyPV7t35MvcgT3W8Q"])
feed_list.append(["Techlore","https://www.youtube.com/feeds/videos.xml?channel_id=UCs6KfncB4OV6Vug4o_bzijg"])
feed_list.append(["Techmoan","https://www.youtube.com/feeds/videos.xml?user=Techmoan"])
feed_list.append(["Lars Muhl","https://www.youtube.com/feeds/videos.xml?channel_id=UCbi5bIFlsLEHwTtzmkBaJ_A"])


def handle_date_string(input_string):
    
    split_string = input_string.split('T')
    split_date = split_string[0].split('-')
    split_time = split_string[1].split('+')[0].split(':')

    return datetime(int(split_date[0]),int(split_date[1]),int(split_date[2]),int(split_time[0]),int(split_time[1]),int(split_time[2]))


def mix_feeds():

    found_feeds = []

    for one_feed in feed_list:

        item_list = feedparser.parse(one_feed[1])["entries"]
        
        for item in item_list:

            found_feeds.append([handle_date_string(item["published"]),item["title"], item["link"], one_feed[0]])
    
    return sorted(found_feeds, reverse=True)
    
def get_feeds():

    feeds = []

    feed_mix = mix_feeds()

    index = 0;

    for f in feed_mix:
        
        date, title, link, feed_name = f
        
        feeds.append([index, date, title, link, feed_name ])

        index = index + 1

    return feeds



def show_feed_list(feed_list):

    #feed_list = get_feeds()

    for f in feed_list:

        count, date, title, link, feed_name = f

        print("%s | %s | %s" % (count, title, feed_name))



def cmd():

    print("? = help | biztube :>", end="")
    command = input()
    return command

if __name__ == "__main__":

    feed_list = get_feeds()

    #feeds = mix_feeds()

    #for f in feeds:
     #   print(f)

    command = None

    while command != 'q':

        command = cmd()

        if command == "list":
            show_feed_list(feed_list)

        elif command == "?":

            print("list         : print video list")
            print("play number  : play a video")
            print("stop         : stop video")
        
        elif command.split(" ")[0] == "play":
            
            number = int(command.split(" ")[1])
            #print("catt -d Tv cast %s" % (feed_list[number][3]))
            os.system("catt -d Tv cast -f %s" % (feed_list[number][3]))
        elif command == "stop":

             os.system("catt -d Tv stop")
