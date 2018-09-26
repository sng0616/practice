import requests
from keys import google as GBooks_Key

pros_ISBN = raw_input("Please enter an ISBN. ")

# A function that takes an ISBN and finds the corresponding book if the ISBN is in use
def find_book_isbn(pros_ISBN):
	GBooks_API = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
	fields = "items/volumeInfo(title, authors, pageCount, categories, publisher), items/searchInfo(textSnippet)"
	GBooks_URL = GBooks_API + pros_ISBN + "&key=" + GBooks_Key + "&fields=" + fields
	GBooks_JSON = requests.get(GBooks_URL).json()['items'][0]
	title, authors, page_count, genre, summary = GBooks_JSON['volumeInfo']['title'], ', '.join(GBooks_JSON['volumeInfo']['authors']), GBooks_JSON['volumeInfo']['pageCount'], ', '.join(GBooks_JSON['volumeInfo']['categories']), GBooks_JSON['searchInfo']['textSnippet']
	return title, authors, page_count, genre, summary
	
# A function that encodes unicode objects and replaces poorly encoded characters to quotes
def encode_str(json_output):
	return [x.encode('ascii','ignore').replace('&quot;','"').replace('&#39;','\'') if isinstance(x, unicode) else x for x in json_output]
	
try:
	print encode_str(find_book_isbn(pros_ISBN))	
except KeyError:
	print "This book is no additional data available through Google Books."
except UnboundLocalError:
	print "Publisher information is unavailable."