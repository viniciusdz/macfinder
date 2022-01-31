#macfinder.py
# Site:          https://github.com/viniciusdz
# Linkedin:      https://www.linkedin.com/in/viniciusdz/
# Written by:    Vinicius Santana
# Maintenance:   Vinicius Santana

import sys
import os
import requests
import time

def search_mac(mac_address):
	vendor = requests.get('http://api.macvendors.com/' + mac_address).text
	return vendor
	
def main():
	fileP = sys.argv[1]
	if not os.path.isfile(fileP):
		print(" Error: File not found !".format(fileP))
		sys.exit()
	
	with open(fileP) as fp:
		line = fp.readline()
		cnt = 1
		while line:
			time.sleep(3)
			vdr = search_mac(line)
			print("MAC: {} - VENDOR: {}".format(line.strip(),vdr))
			line = fp.readline()
			cnt += 1			
main()
