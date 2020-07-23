#Jangan ganti author , hargai creator cape loh buat nya

import requests,os,re

b="\033[0;34m"
g="\033[1;32m"
w="\033[1;32m"
r="\033[1;34m"
y="\033[1;33m"
cyan = "\033[0;36m"
lgray = "\033[0;37m"
dgray = "\033[1;30m"
ir = "\033[0;101m"
reset = "\033[0m"


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}



def turkey():
    global page
    res = requests.get('https://www.insecam.org/en/bycountry/TR/', headers=headers)
    findpage = re.findall('"?page=",\s\d+', res.text)[1]
    rfindpage = findpage.replace('page=", ', '')
    os.system('clear')
    os.system('figlet "HACK CCTV" | lolcat')
    print("{}  '--------------'----------{}------------------.  ").format(r,w)
    print("{}  | {}Author  : {}MRROBO28 {}     | {}INDO{}N{}{}ESIA         | ").format(r,w,r,w,r,ir,reset,w)
    print("{}  | {}Youtube : {}TEKTRIKBOT CN {}| {}@irshad_faqih {}|").format(r,w,w,w,lgray,w)
    print("{}  '------------------------------------{}-------'  ").format(r,w)
    print("{}       [ {}List page : {} {}]").format(r,w,rfindpage,r)
    run()
    
def run():
    try:
        page = input("\033[1;31m       [ \033[1;37mPage \033[1;31m]\033[1;37m> ")
        url = ("https://www.insecam.org/en/bycountry/TR/?page="+str(page))
        print ""
        res = requests.get(url, headers=headers)
        findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
        count = 1
        for _ in findip:
             hasil = findip[count]
             print ("{}[ {}{} {}]").format(r,w,hasil,r)
             count += 1
    except:
        print ""
        print r+"Makasi udh pake tools kami"+w
