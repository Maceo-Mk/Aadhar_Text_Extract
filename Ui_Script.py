import pytesseract
from PIL import Image
import datetime
import cv2
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import os.path
import re
import numpy as np

#Extract name from aadhar

def is_aadhar_card(text):
               text = text.upper()
              # print(text)
               res=text.split()
              # print(res)
               dates={}           
               if 'GOVERNMENT OF INDIA' in text:
                   print ("Aadhar card is valid and the details are below:")
                   index=res.index('INDIA')
                   name=''
                   if (res[index+3].isalpha()):
                     # print(res[index+3])
                      name= res[index+4] + " " + res[index+5] + " " + res[index+6]
                   else :
                      name= res[index+4] + " " + res[index+5] + " " + res[index+6]
               else:
                    name=res[2] + " " + res[3]
               if len(name)>1:
                   print("Name :  " + name)
                   return("Name :  " + name)
               else:
                    print("Name not read")
                    return ("Name not read")

#Extract DOB/YOB 

def Year(text):
    res=text.split()
    if 'Year of Birth' in text:
        inde=res.index('Birth')
        yob=''
        res[inde+2].isalpha()
        yob= res[inde+2] 
        print("Year of Birth:  " + yob)
        return("Year of Birth:  " + yob)
    else:
        p = re.compile('\d+/\d+/\d+')
        if (p.findall(text)):
            dates=p.findall(text)
        if len(dates)>0 and len(dates[0])>1:
           print("Date of birth : "+ str(dates[0]))
           return("Date of birth : "+ str(dates[0]))

#Extract Aadhar number

def number(text):
    text = text.upper()
    res=text.split()
    aadhar_number=''
    '''if 'Male' or 'Female' in res:
        lst = res[-3:]
        print(lst)'''
    i=0
    fres=0
    cou=len(res)
    for i in range(cou):
        if((res[i]=='MALE' or res[i]=='FEMALE') and fres==0):
            fres=1
        if(fres==1 and res[i].isdigit() and len(aadhar_number)<15):
            aadhar_number = aadhar_number + res[i] + ' '
    
    if len(aadhar_number) >= 13:
        print ("Aadhar Number : "+aadhar_number)
        return ("Aadhar Number : "+aadhar_number)
    else:
         print("Aadhar number not read")
         return ("Aadhar number not read")

def main():
    
     #Extract text from Aadhar using Tesseract 
     
     pytesseract.pytesseract.tesseract_cmd = r'C:/Users/sys_name/AppData/Local/Tesseract-OCR/tesseract.exe'
     img = cv2.imread("C:\\Users\\sys_name\\AppData\\Local\\Programs\\Python\\Python36\\123.jpg", cv2.IMREAD_UNCHANGED)
    
     # resize image
    
     resized = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
     img = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
     txt= pytesseract.image_to_string(img, lang='eng')
     #print (txt)
     text= is_aadhar_card(txt)
     text= Year(txt)
     text= number(txt)
main()
    

            
