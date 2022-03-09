#!/usr/bin/env python

# Importare moduli
from requests_html import HTMLSession 
import re
from bs4 import BeautifulSoup as BS
from bs4 import Comment
import requests
from bs4 import BeautifulSoup

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

def printascii():
    print("""
    ___               __    __       __                                    
  / __\___  _ __ ___/ / /\ \ \_ __ / _\ ___ _ __ __ _ _ __   ___ _ __     
 / /  / _ \| '_ ` _ \ \/  \/ / '_ \\ \ / __| '__/ _` | '_ \ / _ \ '__|    
/ /__| (_) | | | | | \  /\  /| |_) |\ \ (__| | | (_| | |_) |  __/ |       
\____/\___/|_| |_| |_|\/  \/ | .__/\__/\___|_|  \__,_| .__/ \___|_|       
                             |_|                     |_|                                   
            
               By Luca Romano - CyberAuror                        
          """)

printascii()

# Indirizzo sito web
url= input('Inserisci il sito-web target:   ')
# Eseguire richiesta GET
response = requests.get(url)
# Analizzare documento HTML del codice sorgente con BeautifulSoup
html = BeautifulSoup(response.text, 'html.parser')
    
comments = html.find_all(string=lambda text: isinstance(text, Comment))
for index,comment in enumerate(comments):
    print("")
    print("------->","Commento", index+1, ":")
    print("")
    print(comment)
    print("")
    print("----------------------------------------------------------------------------------------------------")
    print("")
    comment.extract()




    
    
