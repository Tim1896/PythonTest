import urllib.request
from bs4 import BeautifulSoup

url = "https://bitcoinwisdom.com/"

page = urllib.request.urlopen(url)

soup = BeautifulSoup(page, "html.parser")


def readfnc(market):
    if market in "Bitstamp":
        for child in soup.find(id="market_bitstampbtcusd"):
            return print("Bitstamp USD/BTC:", child)
    if market in "Bitfinex":
        for child in soup.find(id="market_bitfinexbtcusd"):
            return print("Bitfinex USD/BTC:", child)


def checklength(checkstring):
    if len(checkstring) > 3:
        readfnc(checkstring)
    else:
        print("Please type at least 4 Letters.")
        start()



def start():
    userinput = input("Market?: ")
    checklength(userinput)


start()
