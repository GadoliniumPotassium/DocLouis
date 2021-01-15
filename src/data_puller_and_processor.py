import re
import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher

## to get the div set the command is 
## divTag = soup.find_all("div", {"class": ""})
## from this we can get all the moves a character has and isolate the move and data we need.

txtFile=open("src/mvname.txt","r")
moveList=txtFile.readlines()

def get_all_moves(site):
    site_data=requests.get(site)
    soup=BeautifulSoup(site_data.text,'html.parser')
    all_moves=soup.find_all("div",{"class":"movecontainer"})
    return all_moves

def isolate_req_move(all_moves,req_move):
    for move in moveList:
        print (move)
        if req_move in str(move):
            print("in")
            a=move.split(":")
            print(a)
            req_move=a[0]
            print (req_move)
            break
    
    move=""
    for move in all_moves:
        if str(req_move).lower() in str(move).lower():
            break

    return False


