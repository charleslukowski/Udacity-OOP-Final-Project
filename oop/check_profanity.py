
# open file
# split text on spaces to create list of words
# compare list of words from file to list of words in curse list
import urllib

def check(text):
	conn = urllib.urlopen('http://www.wdyl.com/profanity?q='+text)
	output = conn.read()
	conn.close()
	return output

with open('check_this_file.txt', 'r') as f:
	contents = f.read()
f.close()

print check(contents)

