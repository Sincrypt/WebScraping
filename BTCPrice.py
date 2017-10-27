import bs4 as bs
import urllib.request
import time

outfile = 'BTCPrice.txt'

sauce = urllib.request.urlopen('https://cryptowat.ch/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

price = soup.find_all("div", class_="rankings-col__header__segment")
print(price)

while True:
    with open(outfile, 'a+') as f:
        f.write(str(price))

    time.sleep(30)

