import csv
import datetime
from dateutil import parser



ifile = open('test.csv', 'r')
ofile = open('solution.csv', 'w')
reader = csv.reader(ifile)
writer = csv.writer(ofile)
listofrows = list(reader) #convert reader to list
    
statesfile = open('state_abbreviations.csv', 'r')
s_reader = csv.reader(statesfile)
states_dictionary = dict(s_reader) #create a dictionary from the state abbrev csv

#create a function to ensure only full dates(M, D, Y) can be parsed
def parse_no_default(dt_str):
  dt = parser.parse(dt_str, default=datetime.datetime(1900, 1, 1)).date()
  dt2 = parser.parse(dt_str, default=datetime.datetime(1901, 2, 2)).date()
  if dt == dt2:
    return dt
  else:
    raise ValueError('missing a date parameter')


rownum = 0
for row in listofrows:
    #special case of header
    if rownum == 0:
        row.append('start_date_description')
    else:
        #split bio between whitespace, then join with single space
        row[-3] = ' '.join(row[-3].split())
        #use dict to replace abbreviations with full state names
        row[5] = states_dictionary.get(row[5], 'Invalid State')
        #format valid dates
        try:
            date = parse_no_default(row[-1])
            row[-1] = str(date)
            row.append('')
        #filter invalid dates into the new column
        except:
            row.append(row[-1])
            row[-2] = ''
    writer.writerow(row)
    rownum += 1
    
statesfile.close()
ifile.close()
ofile.close()
