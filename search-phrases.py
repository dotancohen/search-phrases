#!/usr/bin/python3

"""
Search a given URL for phrases in specific locations on the page. This is useful for checking a news feed.
"""

import urllib.request
from bs4 import BeautifulSoup

match_file = '/home/foobar/search-phrases-data.txt'

url = 'http://example.com/page.html'
search_phrases_dict = {
	'.titles': ['foo bar', 'baz'],
	'.people': ['Linus Torvalds', 'Archimedes']
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

