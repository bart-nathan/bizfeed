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

            pub_date = handle_date_string(item["published"])

            if is_today(pub_date):

                found_feeds.append([pub_date,item["title"], item["link"], one_feed[0]])
    
    return sorted(found_feeds, reverse=False)
    
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

    for f in feed_list:

        count, date, title, link, feed_name = f

        print("%s | %s | %s | %s" % (count, date,title, feed_name))

def cmd():

    print("? = help | biztube :>", end="")
    command = input()
    return command

def display_menu():

    feed_list = get_feeds()
    show_feed_list(feed_list)

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
            os.system("catt -d Tv cast -f %s" % (feed_list[number][3]))
        
        elif command == "stop":

             os.system("catt -d Tv stop")

if __name__ == "__main__":

    display_menu()
    