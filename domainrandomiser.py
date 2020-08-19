import requests
import colorama
colorama.init()
from colorama import Fore, Style
import random
import time
while True:
	randoming1 = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890")
	randoming2 = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890")
	randoming3 = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890")
	randoming4 = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890")
	randoming5 = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890")
	randoming6 = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890")
	randoming7 = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890")
	randoming8 = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890")
	randoming9 = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890")
	randoming10 = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890")
	randoming11 = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890")
	randoming12 = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890")
	time.sleep(1)
	
	domain = ("http://www." + randoming1 + randoming2 + randoming3 + randoming4 + randoming5 + ".com")
	domain = domain
	
	print(Fore.BLUE + ' Checking: ' + Fore.CYAN + domain + Style.RESET_ALL)
	try:
		request = requests.get(domain)
		print(Fore.LIGHTRED_EX + '\tTAKEN' + Style.RESET_ALL)
	except:
		print(Fore.LIGHTGREEN_EX + '\tFREE' + Style.RESET_ALL)
