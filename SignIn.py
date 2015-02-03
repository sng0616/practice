import csv
# From Shannon's GitHub - "csv_to_dict.py"

filename = "STPSignIn.csv"
def csvtodict(filename):
    
    with open(filename, 'r') as csv_file:
        text = csv_file.read().strip().split('\r')

    header_row = text[0].split(',')
#    print header_row
    dictionary = {}

    for row, line in enumerate(text[1:]):
    
# Get rid of commas in csv; avoid commas in csv files in the future - Done!
		
		dictionary[row] = {}
		
#		print line
		
		for col, cell in enumerate(line.split(',')):

			dictionary[row][header_row[col]] = cell

			if dictionary[row][header_row[col]] == '':
				dictionary[row][header_row[col]] = "N/A"
    return dictionary		

super_dict = csvtodict("STPSignIn.csv")

with open(filename, 'r') as meh:
	firstcsv = meh.read().strip().split('\r')
	fieldnames = firstcsv[0].split(',')

halp = open("struggle_file.csv", "w")
back2csv = csv.DictWriter(halp, delimiter = ",", fieldnames = fieldnames)
for key, values in super_dict:
	back2csv


'''

import csv


#	If you get this to work, make this into a function to use later.


with open("STPSignIn.csv", "r") as perm_file:
	fieldnames = ('#','Event Name','Event Type', 'ActionKit Name', 'Date of Event', 'City',	'First Name', 'Last Name', 'Email Address', 'Phone Number', 'Street Address	City', 'State', 'ZIP Code', 'US District', 'Action_ID', 'User_ID', 'Emerging Majority', 'Attended Event?','# of Events Attended', 'Job Placement Interest', 'Training Interest',	'Volunteered to train/coach?')
	csv_dict=csv.DictReader(perm_file, delimiter = '\r')
#	print vars(csv_dict)
	next(perm_file, None)
#	print vars(csv_dict)
	print csv_dict
#	rows = []
#	for row in csv_dict:
#		print row
#		if row['Job Placement Interest'] == None:
#			row['Job Placement Interest'].replace(None, "N/A")
#		rows.append(row)
#	print rows
#	write_it = csv.DictWriter(open('please_work.csv', 'w'), fieldnames)
#	write_it.writerows(rows)


#with open('eggs.csv', 'rb') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print ', '.join(row)
	
'''

'''
with open('test.csv') as f:
    fieldnames = ('variable', 'name', 'date', 'location', 'youtube')
    r = csv.DictReader(f, fieldnames)
    next(f, None) # skip header
    rows = []
    for row in r:
        if row['variable'] == 'e1':
            row['name'] = 'My birthday'
        if row['variable'] == 'e2':
            row['location'] = 'India'
        rows.append(row)
    w = csv.DictWriter(a_file, fieldnames)
    w.writerows(rows)

	keys = []
	for row in csv_dict:
		print row

	for row in csv_dict:
		if csv_dict["Job Placement Interest"]:
			csv_dict["Job Placement Interest"] = "N/A"
		new_dict.writerow(row)
	
	
new_dict = csv.DictWriter(open("bogus.csv", "w"), )
for row in csv_dict:
	if csv_dict["Job Placement Interest"]== "":
		csv_dict["Job Placement Interest"] = "N/A"
	new_dict.writerow(row)
'''