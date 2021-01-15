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
    soup=BeautifulSoup(site_data.text,'lxml')
    all_moves=soup.find_all("div",{"class":"movecontainer"})
    return all_moves

def filter_data(data):
    data_string=""
    soup=BeautifulSoup(str(data),'lxml')
    movename=soup.find_all("div",{"class" : "movename"})[0].text.strip()
    startup=soup.find_all("div",{"class":"startup"})[0].text.strip()
    total_frames=soup.find_all("div",{"class":"totalframes"})[0].text.strip()
    landing_lag=soup.find_all("div",{"class":"landinglag"})[0].text.strip()
    base_damage=soup.find_all("div",{"class":"basedamage"})[0].text.strip()
    notes=soup.find_all("div",{"class":"notes"})[0].text.strip()
    shield_lag=soup.find_all("div",{"class":"shieldlag"})[0].text.strip()
    shield_stun=soup.find_all("div",{"class":"shieldstun"})[0].text.strip()  
    on_shield=soup.find_all("div",{"class":"advantage"})[0].text.strip()
    active_frame=soup.find_all("div",{"class":"activeframes"})[0].text.strip()
    whichhitbox=soup.find_all("div",{"class","whichhitbox"})[0].text.strip()
    
    #now we are going to fill the data string with all the information and then return it
    data_string = "this move is "+ movename + "\nit starts up on frame(s) "+startup + "\nit lasts for "+total_frames+" frames with frame(s) " + active_frame + " being the active frame(s)\n"+ "it has "+landing_lag+" frames of landing lag\n"+ "it has base damage of "+base_damage+"\n"+ "it has " + shield_lag + "frames of shield lag and " + shield_stun + " frames of shield stun\n" + "it is also " + on_shield + " frames on shield.\n"+ "Important to note on this move is that " + notes+ "." + "special note:" + whichhitbox 
    print(data_string)
    return data_string


def isolate_req_move_post_data(all_moves,req_move):
    move_exists=False
    for move in moveList:
        if req_move in str(move):
            a=move.split(":")
            req_move=a[0]
            break
    
    move=""
    move_div=""
    for move in all_moves:
        if str(req_move).lower() in str(move).lower():
            move_exists=True
            move_div=move
            break

    if move_exists==False: 
        return "Sorry baby, I don't know what you're talking about."

    return filter_data(move_div) 
