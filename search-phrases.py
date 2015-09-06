#!/usr/bin/python3

import urllib.request
from bs4 import BeautifulSoup

url = 'http://www.ynet.co.il/home/0,7340,L-184,00.html'
match_file = '/home/dotancohen/.bin/ynet-search-phrases-data.txt'
search_phrases = ['אופניים חשמליים', 'באר שבע', 'אשכולות']



def main(url, search_phrases, match_file):
	matches = []
	response = urllib.request.urlopen(url)
	response_text = response.read().decode('utf-8')

	soup = BeautifulSoup(response_text, 'html5lib')
	titles = soup.select('.smallheader')

	for t in titles:
		#if 'אופניים חשמליים' in str(t):
		for phrase in search_phrases:
			if phrase in str(t):
				matches.append(str(t))
	
	write_matches(matches, match_file)

	return True



def write_matches(matches, match_file):

	io_file = open(match_file, 'r+')
	existing_matches = io_file.read().split('\n')

	for match in matches:
		if not match in existing_matches:
			io_file.write(match+'\n')

	return True



if __name__=='__main__':
	main(url, search_phrases, match_file)

