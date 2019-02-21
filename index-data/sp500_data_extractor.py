from bs4 import BeautifulSoup
from selenium import webdriver
import scrape_util as u
from time import sleep


def extract_current_sp500():
    url = 'https://finance.yahoo.com/quote/%5EGSPC/'
    soup = u.soup_maker_webdriver(url)

    if not soup:
        return

    header = soup.find(name='div', attrs={'id': 'Lead-2-QuoteHeader-Proxy'})

    price = header.find(
        name='span',
        attrs={'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}
    ).text
    
    print("S&P 500 Price: {}".format(price))

    try: 
        return float(price.replace(',', ''))
    except: 
        return None


def main():
    price = extract_current_sp500()
    if price:
        print(price)


if __name__ == '__main__':
    main()
