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

def filter_data(data):
    soup=BeautifulSoup(data.text,'html.parser')
    data_string=""
    movename=soup.find_all("div",{"class":"movename"})[0].text
    startup=soup.find_all("div",{"class":"startup"})[0].text
    total_frames=soup.find_all("div",{"class":"totalframes"})[0].text
    landing_lag=soup.find_all("div",{"class":"landinglag"})[0].text
    base_damage=soup.find_all("div",{"class":"basedamage"})[0].text
    notes=soup.find_all("div",{"class":"notes"})[0].text
    shield_lag=find_all("div",{"class":"shieldlag"})[0].text
    shield_stun=find_all("div",{"class":"shieldstun"})[0].text    
    on_shield=find_all("div",{"class":"advantage"})[0].text
    active_frame=find_all("div",{"class":"activeframes"})[0].text
    whichhitbox=find_all("div",{"class","whichhitbox"})[0].text
    
    #now we are going to fill the data string with all the information and then return it
    data_string = "this move is "+ movename + "\nit starts up on frame "+startup + "\nit lasts for "+total_frames+" frames with " + active_frame + "being the active frames\n"+ "it has "+landing_lag+" frames of landing lag\n"+ "it has base damage of "+base_damage+"\n"+ "it has " + shield_lag + "frames of shield lag and " + shield_stun " frames of shield stun\n" + "it is also " + on_shield + " frames on shield.\n"+ "important to note on this move is that " + notes+ "." 
    return data_string


def isolate_req_move_post_data(all_moves,req_move):
    move_exists=False
    for move in moveList:
        if req_move in str(move):
            a=move.split(":")
            print(a)
            req_move=a[0]
            print (req_move)
            break
    
    move=""
    for move in all_moves:
        if str(req_move).lower() in str(move).lower():
            move_exists=True
            break
    
    print(move)   
    if move_exists==False: 
        return "Sorry baby, I don't know what you're talking about."
    
    return filer_data(move):

