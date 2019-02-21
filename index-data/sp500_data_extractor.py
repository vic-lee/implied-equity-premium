from bs4 import BeautifulSoup
from selenium import webdriver
import scrape_util as u
from time import sleep



def extract_current_sp500():
    url = 'https://finance.yahoo.com/quote/%5EGSPC/'
    soup = u.soup_maker_webdriver(url) if not None else None
    
    header = soup.find(name='div', attrs={'id': 'Lead-2-QuoteHeader-Proxy'})
    price = header.find(
        name='span', 
        attrs={'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}
    )
    print("S&P 500 Price: {}".format(price.text))


def main():
    extract_current_sp500()


if __name__ == '__main__':
    main()
