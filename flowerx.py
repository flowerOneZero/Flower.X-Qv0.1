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
#from urllib.parse import urlencode
import platform
import time
import colorama
from colorama import init
import progress

init()
print(Fore.RED + "FILE CHECK")
print(Style.RESET_ALL)
for i in [ 1, 2, 3 ]:
        print("Waiting for %s" % i , end='')
        print(Fore.YELLOW + " ><")
        print(Style.RESET_ALL)
        time.sleep(i)
os.system("clr||clear")
message = Fore.GREEN + "START OPSR CODE"
for p in message:
        print(p)
        time.sleep(0.1)
time.sleep(2)
os.system("clr||clear")

import time
from progress.bar import ShadyBar

mylist = [1,2,3,4,5]

bar = ShadyBar(Fore.MAGENTA + 'Load Files:', max = len(mylist))

for item in mylist:
    bar.next()
    time.sleep(0.2)

bar.finish()

os.system("clr||clear")
print(Fore.MAGENTA + Style.DIM + "")
print("     ███████╗██╗░░░░░░█████╗░░██╗░░░░░░░██╗██╗░░██╗")
print("    ██╔════╝██║░░░░░██╔══██╗░██║░░██╗░░██║╚██╗██╔╝")
print("    █████╗░░██║░░░░░██║░░██║░╚██╗████╗██╔╝░╚███╔╝░")
print("    ██╔══╝░░██║░░░░░██║░░██║░░████╔═████║░░██╔██╗░")
print("     ██║░░░░░███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░██╔╝╚██╗")
print("     ╚═╝░░░░░╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝")
print(Fore.GREEN + Style.DIM + "            dev: LilKr0k0dil :: ENDTERROR")
print(Style.RESET_ALL)

sleep(1);
