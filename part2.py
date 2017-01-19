from bs4 import BeautifulSoup
import requests
import json

company_data = {}

for i in range(1, 2):
    url = 'http://data-interview.enigmalabs.org/companies/?page=' + str(i)
    # looping through the 10 pages
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    companies = soup.find_all(id=True) #find all tags with an id attribute
    for company in companies:
        company_url = 'http://data-interview.enigmalabs.org' + company.get('href')
        rr = requests.get(company_url)
        subsoup = BeautifulSoup(rr.content, 'lxml')
        company_name = subsoup.find(id='name').string #company name
        address_line_1 = subsoup.find(id='street_address').string
        address_line_2 = subsoup.find(id='street_address_2').string
        city = subsoup.find(id='city').string
        state = subsoup.find(id='state').string
        zipcode = subsoup.find(id='zipcode').string
        phone = subsoup.find(id='phone_number').string
        company_website = subsoup.find(id='website').string
        company_description = subsoup.find(id='description').string
        company_data[company_name] = {'Address Line 1': address_line_1, 
                                    'Address Line 2': address_line_2,
                                    'City': city,
                                    'State': state,
                                    'Zipcode': zipcode,
                                    'Phone': phone,
                                    'Company Website': company_website,
                                    'Company Description': company_description}

with open('solution.json', 'w') as fp:
    json.dump(company_data, fp, sort_keys=True)
