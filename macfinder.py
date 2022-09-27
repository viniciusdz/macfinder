#macfinder.py
# Site:          https://github.com/viniciusdz
# Linkedin:      https://www.linkedin.com/in/viniciusdz/
# Written by:    Vinicius Santana
# Maintenance:   Vinicius Santana

import re
import string
import sys
import os
import requests
import time


def search_mac(mac_address):
	vendor = requests.get('http://api.macvendors.com/' + mac_address).text
	return vendor
	
def searchList(fileP):
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

def main():

	cmd = sys.argv

	if (cmd[1] == "-h" or cmd[1] == "--help"):
		print("Usage example: \n")
		print("-f FILENAME or --file FILENAME for search vendor from a list of mac address. \n")
		print("-m MACADRESS or --m MACADRESS for search vendor from a mac adress \n")

	if (cmd[1] == "-f" or cmd[1] == "--file"):
		fileP = cmd[2]
		searchList(fileP)

	if (cmd[1] == "-m" or cmd[1] == "--mac"):
		macAdress= cmd[2]
		print("MAC: {} - VENDOR: {}".format(macAdress,search_mac(macAdress)))
	
main()
