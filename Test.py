import urllib.request
from bs4 import BeautifulSoup

url = "https://bitcoinwisdom.com/"

page = urllib.request.urlopen(url)

soup = BeautifulSoup(page, "html.parser")


def bitstampdel():
    with open("bitstampcmp.txt", "r") as f:
        lines = f.read().splitlines()
        if len(lines) > 9:
            f.close()
            w = open("bitstampcmp.txt", "w")
            for line in lines:
                w.write("")


def bitfinexdel():
    with open("bitfinexcmp.txt", "r") as f:
        lines = f.read().splitlines()
        if len(lines) > 9:
            f.close()
            w = open("bitfinexcmp.txt", "w")
            for line in lines:
                w.write("")


def readfnc(market):
    if market == "Bitstamp":
        for child in soup.find(id="market_bitstampbtcusd"):
            bitstampcmp(child)
            bitstampdel()
            writebitstamp(child)
            return print("Bitstamp USD/BTC:", child)
    if market == "Bitfinex":
        for child in soup.find(id="market_bitfinexbtcusd"):
            bitfinexcmp(child)
            bitfinexdel()
            writebitfinex(child)
            return print("Bitfinex USD/BTC:", child)
    else:
        print("This market does not exist.")
        start()


def checklength(checkstring):
    if len(checkstring) > 3:
        readfnc(checkstring)
    else:
        print("Please type at least 4 Letters.")
        start()


def bitstampcmp(tocompare):
    with open("bitstampcmp.txt", "r") as f:
        lines = f.read().splitlines()
        if len(lines) == 0:
            print("nothing to compare")
        else:
            lastline = lines[-1]
            if lastline > tocompare:
                print("↓")
            elif lastline < tocompare:
                print("↑")
            else:
                print("→")


def bitfinexcmp(tocompare):
    with open("bitfinexcmp.txt", "r") as f:
        lines = f.read().splitlines()
        if len(lines) == 0:
            print("nothing to compare")
        else:
            lastline = lines[-1]
            if lastline > tocompare:
                print("↓")
            elif lastline < tocompare:
                print("↑")
            else:
                print("→")


def writebitstamp(towrite):
    with open("bitstampcmp.txt", "a") as f:
        f.write("%s\n" % towrite)
    f.close()


def writebitfinex(towrite):
    wrtfile = open("bitfinexcmp.txt", "a")
    wrtfile.write("%s\n" % towrite)
    wrtfile.close()


def start():
    userinput = input("Market?: ")
    checklength(userinput)


start()
