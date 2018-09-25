#Related to ISBN_valid.py and ISBN_generate.py

import requests
from keys import google as GBooks_Key

GBooks_API = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
pros_ISBN = raw_input("Please enter a 10-digit ISBN. ")

def find_book(pros_ISBN):
    GBooks_URL = GBooks_API + pros_ISBN + "&key=" + GBooks_Key
    GBooks_JSON = requests.get(GBooks_URL).json()
    for book, info in GBooks_JSON.items():
		items_list = GBooks_JSON['items'][0]
		for stuff, more_stuff in items_list.items():
			more_info = items_list['volumeInfo']
			for this, that in more_info.items():
				title = more_info['title'].encode('ascii','ignore')
				authors = more_info['authors']
				if len(authors) > 1:
					authors = more_info['authors']
				else:
					authors = more_info['authors'][0].encode('ascii','ignore')
				if 'publishedDate' in more_info:
					publish_date = more_info['publishedDate']
				else:
					pass
				if 'publisher' in more_info:
					publisher = more_info['publisher'].encode('ascii','ignore')
				else:
					pass
				plot = more_info['description'].encode('ascii','ignore')
				ISBN_list = more_info['industryIdentifiers']
				ISBN_dict10 = more_info['industryIdentifiers'][0]
				ISBN_dict13 = more_info['industryIdentifiers'][1]
				for lah, dee in ISBN_dict10.items():
					ISBN10 = ISBN_dict10['identifier']
				for boo, hoo in ISBN_dict13.items():
					ISBN13 = ISBN_dict13['identifier']
#    Use partial response to get desired fields
    print title +"\n"+ authors +"\n"+ publish_date +"\n"+ publisher +"\n"+ ISBN10 +"\n"+ ISBN13 +"\n"+plot


try:
    find_book(pros_ISBN)
except KeyError:
	print "This book is not available through Google Books."
except UnboundLocalError:
	print "Publisher information is unavailable."

