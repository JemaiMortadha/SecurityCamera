import os
import time
import requests
from PIL import *
from cv2 import *
from datetime import *
print("""\033[93m
 ____        __  __            _            _ _           
|  _ \      |  \/  |          | |          | | |          
| |_) |_   _| \  / | ___  _ __| |_ __ _  __| | |__   __ _ 
|  _ <| | | | |\/| |/ _ \| '__| __/ _` |/ _` | '_ \ / _` |
| |_) | |_| | |  | | (_) | |  | || (_| | (_| | | | | (_| |
|____/ \__, |_|  |_|\___/|_|   \__\__,_|\__,_|_| |_|\__,_|
        __/ |                                             
       |___/      Facebook.com/mortadha.jemai
                       
 {a}Motion Detect {b}- {a}Get Images On Telegram {b}*
 
""".format(a="\033[92m", b="\033[94m"))
def sendImage():
    url = "https://api.telegram.org/bot1207025001:AAETpX1xSUqmlwM9Jysa0u61FzNYEXaMlA0/sendPhoto";
    files = {'photo': open(str(new_folder)+'/'+str(dn)+'.png', 'rb')}
    data = {'chat_id' : "-345181111"}
    r= requests.post(url, files=files, data=data)
    #print(r.status_code, r.reason, r.content)
d=datetime.now()
location=os.getcwd()
new_folder=location+'/'+str(d.date())
newpath = new_folder
if not os.path.exists(newpath):
    os.makedirs(str(new_folder)+'/')
x=0
while x==0 :
  ask=input("Do you want to take a refference image ? (Y/y) if yes , (N/n) if you already have one : ")
  if str(ask)=='Y' or str(ask)=='y':
    import time
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    s,img3=cap.read()
    imwrite(str(location)+'/ref.png',img3)
    cap.release()
    time.sleep(1)
    print('Refference Pic is Ready')
    x+=1
  elif str(ask)=='N' or str(ask)=='n':
    import time
    time.sleep(1)
    x+=1
  else : 
    print("Please take a valid choice")
    
y=0
while y==0 :
  n=input("Please enter waiting time before the motion detection starts (Max 60 seconds) : ")
  if (not n.isdigit()) : 
    print("   ")
  elif (int(n)>=0) and (int(n)<=60) :
    y+=1
    break
for i in range(0,int(n)+1) :
  print (str(int(n)-i))
  time.sleep(1)
  
  
while True :
  cap = cv2.VideoCapture(0)
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
  s,img1=cap.read()
  imwrite(str(new_folder)+'/test1.png',img1)
  s,img2=cap.read()
  imwrite(str(new_folder)+'/test2.png',img2)
  cap.release()
  fs1 = os.stat(str(new_folder)+'/test2.png').st_size
  fs2 = os.stat(str(location)+'/ref.png').st_size
  diff=abs(fs1-fs2)
  import time
  if (diff > 10000):
    print('Movement Detected ! ')
    dn=datetime.now()
    os.rename(str(new_folder)+'/test2.png', str(new_folder)+'/'+str(dn)+'.png')
    os.remove(str(new_folder)+'/test1.png')
    sendImage()
  else: 
    os.remove(str(new_folder)+'/test1.png')
    os.remove(str(new_folder)+'/test2.png')

