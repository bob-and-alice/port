import socket
import time
import requests
from colorama import init, Fore, Back, Style
import threading
import os

def control(ip, port):
    try:
        s = socket.socket()
        s.settimeout(5)
        connect_ = s.connect_ex((ip, port))
        if connect_ == 0:
            print(Fore.GREEN + f"Port Open: {ip}:{port}\n")
        else:
            print(Fore.RED + f"Port Closed: {ip}:{port}\n")
    except Exception as e:
        print(f"hata: {e}")
    finally:
        s.close()


signature = '''
           ;               ,           
         ,;                 '.         
        ;:                   :;        
       ::                     ::       
       ::                     ::       
       ':                     :        
        :.                    :        
     ;' ::                   ::  '     
    .'  ';                   ;'  '.    
   ::    :;                 ;:    ::   
   ;      :;.             ,;:     ::   
   :;      :;:           ,;"      ::   
   ::.      ':;  ..,.;  ;:'     ,.;:   
    "'"...   '::,::::: ;:   .;.;""'    
        '"""....;:::::;,;.;"""         
    .:::.....'"':::::::'",...;::::;.   
   ;:' '""'"";.,;:::::;.'""""""  ':;   
  ::'         ;::;:::;::..         :;  
 ::         ,;:::::::::::;:..       :: 
 ;'     ,;;:;::::::::::::::;";..    ':.
::     ;:"  ::::::"""'::::::  ":     ::
 :.    ::   ::::::;  :::::::   :     ; 
  ;    ::   :::::::  :::::::   :    ;  
   '   ::   ::::::....:::::'  ,:   '   
    '  ::    :::::::::::::"   ::       
       ::     ':::::::::"'    ::       
       ':       """""""'      ::       
        ::                   ;:        
        ':;                 ;:"        
-Deepscrn-     ';              ,;' port checker          
            "'           '"            
              '
'''

print(signature)

init(autoreset=True)

if os.name != 'posix':   
    print(Fore.RED + "This script is designed to run on Linux (GNU) systems only.")
    exit()   

select = input(Fore.CYAN + "Please Select mode\n1-)Scan a specific port number\n2-)Scan favorite ports\n3-)Scan ports within a specific range\n")

match select:

    case "1":

        port = input("Enter Port Number:")
        print("Detecting IP address...")
        time.sleep(2)
        try:
            check = requests.get("https://ifconfig.me/ip")
            print(Fore.GREEN + f"Your IP address is: {check.text}")
            control(check.text, int(port))
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"Error: {e}")

    case "2":
        print(Fore.GREEN + f"Favorit ports to be scanned")
        print("Detecting IP address...")
        time.sleep(2)

        try:
            check = requests.get("https://ifconfig.me/ip")
            ipadress = check.text.strip()
            print(Fore.GREEN + f"Your IP address is: {ipadress}")

            favori = [80, 445, 81, 22]

            threads = []

            for port in favori:
                thread = threading.Thread(target=control, args=(ipadress, port))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"Error: {e}")

    case "3":

        start = input("Start number:")
        end = input("End number:")
        print("Detecting IP address...")
        time.sleep(2)

        try:
            check = requests.get("https://ifconfig.me/ip")
            ipadress = check.text.strip()
            print(Fore.GREEN + f"Your IP address is: {ipadress}")

            threads = []

         
            for port in range(int(start), int(end) + 1):   
                thread = threading.Thread(target=control, args=(ipadress, port))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"Error: {e}")

        
