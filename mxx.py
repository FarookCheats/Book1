import requests,json,time,threading,os,sys
import urllib.request, os, threading, time, random, sys
import colorama
from colorama import Fore, Style, init
#from requests_futures.sessions import FuturesSession
#from requests_futures import sessions
os.system("clear")
print(Fore.YELLOW + "การบ้าน EP1")
print("")
print("กดเลข1เพื่อทำการบ้าน")
verfly = input("Number : ")
if verfly == '1':
	os.system("clear")
	
print(Fore.RED + "สวัสดีครับ ผมพลเอกประยุทธ์ จันโอชา (ผู้ออกข้อสอบ)")
print("")
print(Fore.GREEN + "1) ใครโง่สุดในประเทศไทย?")
number = input("คำตอบของคุณ : ")
print(Fore.RED + "ใช่ครับ")
print(Fore.GREEN + "2)คุณคิดยังไงกับข้อที่1 บ้างครับ?")
number = input("คำตอบของคุณ : ")
print(Fore.RED + "คิดเหมือนกันครับ")
print(Fore.GREEN + "3) 1+1=......")
number = input("คำตอบของคุณ : ")
print(Fore.RED + "ผิดครับ")
print("")
number = input("รวมคะแนน : ")
print(Fore.GREEN + "กำลังประมูล..")
time.sleep(2)
os.system("clear")
time.sleep(2)
print(Fore.YELLOW + "ละนี่คือคะแนนของคุณ..")
time.sleep(3)
print("")
print(Fore.RED + "ผมคิดว่าผมโง่แล้วนะยังมีคนโง่กว่าผมอีกหรอ")