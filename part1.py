import csv

ifile = open('test.csv', 'r')
ofile = open('solution.csv', 'w')
reader = csv.reader(ifile)
writer = csv.writer(ofile)
listofrows = list(reader) #convert reader to list
    
statesfile = open('state_abbreviations.csv', 'r')
s_reader = csv.reader(statesfile)
states_dictionary = dict(s_reader) #create a dictionary from the state abbrev csv

rownum = 0
for row in listofrows:
    if rownum != 0:
        row[-3] = ' '.join(row[-3].split()) #split bio between whitespace, then join with single space
        row[5] = states_dictionary.get(row[5], 'Invalid State')
    writer.writerow(row)
    rownum += 1
    
statesfile.close()
ifile.close()
ofile.close()