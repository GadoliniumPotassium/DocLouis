import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher


##BUG THIS ENTIRE CLASS NEEDS FIXING

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
    image=soup.find_all("a")
    img_link=""
    for x in image:
        img_link+="https://ultimateframedata.com/"+x['data-featherlight']+"\n"
    print(img_link)
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
    data_string =img_link+"\nmovename: "+ movename + "\nstartup frame(s) "+startup + "\nlasts for "+total_frames+"\nActive frames: " + active_frame + "\n"+ "landing lag: "+landing_lag+" frames\n"+ " base damage: "+base_damage+"\n"+ "shield lag:" + shield_lag + " frames\nshield stun:" + shield_stun + "\n" + "on shield:" + on_shield + " frames\n"+ "Note:" + notes + "\nspecial note:" + whichhitbox 
    print(data_string)
    return data_string


def isolate_req_move_post_data(all_moves,req_move):
    move_exists=False
    asked_move=""
    for move in moveList:
        if req_move.lower().strip() in str(move).lower().strip():
            a=move.split(":")
            asked_move=a[0]
            print(asked_move)
            break
            
    move=""
    move_div=""
    info=""
    for move in all_moves:
        if str(asked_move).lower() in str(move).lower():
            print("in here")
            move_exists=True
            move_div=move
            info += filter_data(move_div)
            break

    if move_exists==False: 
        return False

    return info 