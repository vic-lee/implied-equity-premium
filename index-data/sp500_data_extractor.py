from bs4 import BeautifulSoup
from selenium import webdriver
import scrape_util as u
from time import sleep


def main():
    url = 'https://finance.yahoo.com/quote/%5EGSPC/'

    # soup = u.soup_maker(url)
    # price = soup.find(name='table', attrs={'class': 'performance-chart-table'})
    # print(soup)
    # print(price)

    # Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)
    with webdriver.Chrome('_driver/chromedriver') as driver:
        driver.get(url)
        # innerHTML = driver.execute_script("return document.body.innerHTML") 
        # print(innerHTML)
        html_source = driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')

    # print(soup)
    print(soup.find('div', attrs={'id': 'Lead-2-QuoteHeader-Proxy'}))
    # price = price_module.find_element_by_class_name('Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')
    # print(price)



if __name__ == '__main__':
    main()
