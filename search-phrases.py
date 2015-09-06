#!/usr/bin/python3

import urllib.request
from bs4 import BeautifulSoup

match_file = '/home/dotancohen/code/ynet-search-phrases-data.txt' # TESTING
#match_file = '/home/dotancohen/.bin/ynet-search-phrases-data.txt' # PRODUCTION

url = 'http://www.ynet.co.il/home/0,7340,L-184,00.html'
search_phrases_dict = {
	'.smallheader': ['אופניים חשמליים', 'באר שבע', 'אשכולות']
}



def main(url, search_phrases_dict, match_file):
	matches = []
	response = urllib.request.urlopen(url)
	response_text = response.read().decode('utf-8')

	soup = BeautifulSoup(response_text, 'html5lib')

	for css_selectors, search_phrases in search_phrases_dict.items():
		titles = soup.select(css_selectors)
		for t in titles:
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
	main(url, search_phrases_dict, match_file)

