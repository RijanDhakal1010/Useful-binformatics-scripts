# this python script solely exists to interact with the html website http://www.onekp.com/public_data.html
# the script will access the website and then extract the hyperlinks to the peptides we are interested in
# the script is designed to just print to terminal, please use stdout and stdin to extend it

# these are the libraries we will need
import requests
from lxml import html
from bs4 import BeautifulSoup

headers_1 = {'Accept-Encoding': 'identity', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'} # this is need to save us from being hit with captcha
connection_one = requests.get('http://www.onekp.com/public_data.html', headers = headers_1) # this is the website
soup_object = BeautifulSoup(connection_one.content,features="lxml") # this creat a soup object that we will parse

test = soup_object.findAll('a') # this finds all parts of the soup object with 'td'

a = ".faa.tar.bz2" # this is the extension we are looking for
for i in test: # we will loop though the object
    if a in str(i): # this test the object to see if the current sub-object has the extension we are looking for
    	link_one = str(i.get('href'))
    	link_one = link_one.replace('export=download&','')
    	print(link_one) # print if the conditional in the previous line comes out to be true