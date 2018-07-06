from lxml import html
import requests


eia860_url = 'https://www.eia.gov/electricity/data/eia860/'


eia923_url = 'https://www.eia.gov/electricity/data/eia923/'

def years_eia923():    
    page = requests.get(eia923_url)
    tree = html.fromstring(page.content)
    buyers = tree.xpath('//td/text()')
    years = []
    for item in buyers:
        if item[:4].isnumeric():
            years.append(item[:4])
    years.append('2000mu')
    years.append('2000u')
    for i in range(70,100):
        i = str(i)
        if i in ['99' , '98', '97', '96']:
            years.append('19' + i + 'mu')
        years.append('19' + i + 'u')
    
    years[1] = '2017er'
    return years

def years_eia860() :    
    page = requests.get(eia860_url)
    tree = html.fromstring(page.content)
    buyers = tree.xpath('//td/text()')
    years = []
    for item in buyers:
        if item[0].isnumeric(): 
            item = item.replace(" ", "")
            if item.endswith('*'):
                non_utility = 'b' + item[:-1]
                years.append(non_utility)
                item = item[:-1]
            if item in ['2000','1999','1998',
                        '1997','1996','1995',
                        '1994','1993','1992',
                        '1991','1990']:
                item = 'a' + item
            years.append(item)
    
    return years

Years_eia860 = years_eia860()

Years_eia923 = years_eia923()