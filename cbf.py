#!/usr/bin/python3
from optparse import OptionParser
class caesar():
    def encryption(plaintex,key):
        ctext=""
        for i in plaintex:
            if i.isalpha():
                isupper=i.isupper()
                cipher=chr((ord(i)-ord("A" if isupper else "a") +int(key))%26+ord("A" if isupper else "a"))
                ctext += cipher
        print(ctext)

    def CBruteforce(text):
        try:
            text=str(text)
            if text !='':
                for i in range(1,26):
                    caesar.encryption(text,-i)
        except Exception:
            print("invlid value ")

pars= OptionParser("""
  ____ ____  _____ 
 / ___| __ )|  ___|
| |   |  _ \| |_   
| |___| |_) |  _|  
 \____|____/|_|    
                                               
---------------------------
!!!CBF is a tool that decrypts text data using the Caesar cipher
---------------------------
CBF -t + text
Developed by: Ibrahem abo kila
""")
pars.add_option("-t", dest="text")
(options ,args) = pars.parse_args()
if options.text == None:
    print(pars.usage)
else:
    print("""
  ____ ____  _____ 
 / ___| __ )|  ___|
| |   |  _ \| |_   
| |___| |_) |  _|  
 \____|____/|_|    
                                                        
---------------------------
""")
    caesar.CBruteforce(options.text)