from bs4 import BeautifulSoup
from selenium import webdriver
import scrape_util as u
from time import sleep, time


def extract_current_sp500():
    url = 'https://finance.yahoo.com/quote/%5EGSPC/'
    soup = u.soup_maker_webdriver(url=url, headless=True)

    if not soup:
        return

    header_id = 'Lead-2-QuoteHeader-Proxy'
    price_class = 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'
    header = soup.find(name='div', attrs={'id': header_id})
    price = header.find(name='span', attrs={'class': price_class}).text

    try: 
        return float(price.replace(',', ''))
    except: 
        return None


def main():
    start_time = time()
    price = extract_current_sp500()
    if price:
        print("S&P 500 Price: {}".format(price))
    print("Time elapsed: {} seconds.".format(u.seconds_elapsed(start_time)))
    print("Program terminating...")


if __name__ == '__main__':
    main()
