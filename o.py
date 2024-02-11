#المكاتب مئشر بسهم حملهن
import requests#↞							  
import uuid#↞									
import random#↞				 
import time#↞								
import sys#↞								  
import threading,secrets#↞
import sys as n					 
E = '\033[1;31m'
A = '\033[1;33m'
Q = '\033[1;34m'
G = '\033[1;32m'
W = '\033[1;36m'
g ='='*60
print(f"""{G}{g}                      
	                    $$\                 
	                    $$ |                
	 $$$$$$\  $$\   $$\ $$ |  $$\  $$$$$$$\ 
{E}	$$  __$$\ $$ |  $$ |$$ | $$  |$$  _____|
{A}	$$ |  \__|$$ |  $$ |$$$$$$  / \$$$$$$\  
{A}	$$ |      $$ |  $$ |$$  _$$<   \____$$\ 
{E}	$$ |      \$$$$$$  |$$ | \$$\ $$$$$$$  |
{G}	\__|       \______/ \__|  \__|\_______/ 

 The tool is completely free and from the developer of ruks
{g}""")
ruks_ = '\033[1;36m'



username = input(E+'['+A+'+'+E+']'+A+' username :'+G)
password = input(E+'['+A+'+'+E+']'+A+' password :'+G)

u5rl = 'https://www.instagram.com/accounts/edit/'
req=''
def login_ruks():
    uid = uuid.uuid4()
    cookie = secrets.token_hex(8)*2
    r = requests.Session()
    global username
    global password,sessi
    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36', 'x-csrftoken': 'missing', 'mid': cookie}
    data = {'username':username,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
            'queryParams': '{}',
            'optIntoOneTap': 'false',}
    re = r.post(url,headers=headers,data=data)   	    
    if ("userId") in re.text:    
    	print('login True')
    	print('='*20)
    	if 'authenticated":true' in re.text:
    		sessi = r.cookies["sessionid"] 		
    else:
    	print('='*20)
    	print(E+'Error, place the information correct')
    	exit(0)			

#========
login_ruks()
r = 'https://www.instagram.com/accounts/edit/?__a=1'
headers_ruks = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                    'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; ds_user_id=45334757205; rur=VLL; csrftoken=bIgRYPpWJicGXzVLzCoHrxzy0NCe0VJs; sessionid={sessi}',
                    'referer': 'https://www.instagram.com/accounts/edit/',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
                    'x-ig-app-id': '936619743392459',
                    'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9KR4',
                    'x-requested-with': 'XMLHttpRequest'
                }

data_ruks = {
	'__a': '1'}

r_ruks = requests.get(r, data=data_ruks, headers=headers_ruks)
email = str(r_ruks.json()['form_data']['email'])
phone = str(r_ruks.json()['form_data']['phone_number'])
USER=input(E+'['+A+'+'+E+']'+A+' USER :'+G) 
#====:
url = 'https://www.instagram.com/accounts/edit/'	
ruks22 = {
                            'accept': '*/*',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
                            'content-length': '131',
                            'content-type': 'application/x-www-form-urlencoded',
                            'cookie': f'sessionid={sessi}',
                            'origin': 'https://www.instagram.com',
                            'referer': 'https://www.instagram.com/accounts/edit/',
                            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                            'x-csrftoken': 'XGn1DgK0YG2q5Juuy25fphr8ZfuyTmSr',
                            'x-ig-app-id': '936619743392459',
                            'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
                            'x-instagram-ajax': '41d8a89b6f90',
                            'x-requested-with': 'XMLHttpRequest'}


ruks2 = {
	'email': f'{email}',
	'username': f'{USER}',
	'phone_number': f'{phone}',
	'biography': 'ruks ',
	'external_url': '',
	'chaining_enabled': 'on'
              }
def ruks3():
	global ruks2,ruks22,url
	try:
		while True:
			edit = requests.post(url, headers=ruks22, data=ruks2).text		
			if ('{"status":"ok"}') in edit:
				print('Done Swap v3 🇮🇶')
				break
				exit(0)
			else:
				print(E+'He has not been moved !!')
										
	except:
		pass
thread = []
for i in range(50):#سرعة الداة#Tool speed
	thread1 =threading.Thread(target=ruks3)
	thread1.start()
	thread.append(thread1)
for thread2 in thread:
	thread2.join
		
