from lxml import etree
import requests

def get_hrefs(link):
    r = etree.fromstring(requests.get(link).text, etree.HTMLParser())
    hrefs_in_link = []
    for elem in r.iter('a'):
        if 'href' in elem.attrib:
            hrefs_in_link += [elem.attrib['href'].replace('stepic', 'stepik')]
    return hrefs_in_link


A = input().replace('stepic', 'stepik')
B = input().replace('stepic', 'stepik')

for link_in_A in get_hrefs(A):
    print([link_in_A])
    if B in get_hrefs(link_in_A):
        print('Yes')
        break
else:
    print('No')
