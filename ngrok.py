
import os
import sys
import time

os.system("clear")

print("""\033[1;40;31m
              Checking for Internet Connection [+] """)
time.sleep(1)
os.system("clear")

import requests

while True:
    try:
        requests.get('https://www.google.com/').status_code
        break
    except:
        os.system("clear")
        print(""" \n\n   NO INTERNET CONNECTION!  \n\n """)
        exit()

os.system("rm *arm.zip")
os.system("clear")

x = input("""\033[1;32;40m
                  Choose your option! 
                       		             
         Press [1] for Kali   |   Press [2] for Termux


                    >>>  """)

if x =='1':
    os.system("clear")
    os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip && unzip *.zip && chmod +x ngrok && rm -rf *.zip")


elif x =='2':
    os.system("clear")
    os.system("wget https://bin.equinox.io/a/e93TBaoFgZw/ngrok-2.2.8-linux-arm.zip && unzip *.zip && chmod +x ngrok && rm -rf *.zip")

else:
  print("""\033[1;40;31m
                     \n Wrong key entered!""")
  exit() 



y = input("""
            run [exit] to skip Adding Authtoken

            run [add] to Add Authtoken!  >>  """)

if y =='add':

   Y = input("""
           Paste your Authoken and Press enter \n\n >> : """)
   os.system("clear && ./ngrok authtoken "+Y)
   os.system("clear")
   print('\x1b[6;30;42m' +

                       '\n\n  NGROK IS READY  \n\n' +
      '\n From now onwards no need of HOTSPOT for ngrok on TERMUX! \n'
                                
                                         + '\x1b[0m')


elif y =='exit':
         print("""
                  Cancelled!""")+exit()
else:
   print("""\033[1;40;31m
              \n Wrong key entered!""")
   exit()

