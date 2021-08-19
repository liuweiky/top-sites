import requests
from bs4 import BeautifulSoup
import time

top_sites_filename = 'top-sites.txt'
top_sites_url_filename = 'top-sites-url.txt'

f_sites = open(top_sites_filename, 'a', encoding='utf-8')
f_url = open(top_sites_url_filename, 'a', encoding='utf-8')

for rank in range(1000, 1000001, 1000):
    url = ('http://stuffgate.com/stuff/website/top-%d-sites') % (rank)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    tbody = soup.select('body > main > div > div.row > div.col-lg-8 > div.sg-overflow > table > tbody')[0]
    trs = tbody.find_all('tr')
    for tr in trs:
        site = {}
        tds = tr.find_all('td')
        site['rank'] = tds[0].get_text().strip()
        site['domain'] = tds[1].get_text().strip()
        site['url'] = tds[1].find('a').get('href')
        print(site)
        f_sites.write('%s\n' % (site['domain']))
        f_url.write('%s\t%s\t%s\n' % (site['rank'], site['domain'], site['url']))
    # time.sleep(1)

f_sites.close()
f_url.close()
