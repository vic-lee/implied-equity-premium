from bs4 import BeautifulSoup
from urllib import request as re
import csv
import scrape_util as u


def multpl_table_parser(url):
    contents = {}
    soup = u.soup_maker(url)
    rows = soup.find_all('tr')
    for row in rows:
        yr = row.select('td.left')
        data = row.select('td.right')
        if len(yr) > 0 and len(data) > 0:
            yr = yr[0].text[-4:]
            try:
                data = float(data[0].text.strip('\n'))
            except:
                print("Error: data entry may not be a number.")
                continue
            contents[yr] = data
    return contents


def extract_annual_earnings():
    earnings = multpl_table_parser(
        "http://www.multpl.com/s-p-500-earnings/table")
    return earnings


def extract_annual_dividends():
    dvds = multpl_table_parser("http://www.multpl.com/s-p-500-dividend/table")
    return dvds


def main():
    dividends = extract_annual_dividends()
    print(dividends)

    earnings = extract_annual_earnings()
    print(earnings)

    u.dict_to_csv(dividends, '../output/dividends.csv')
    u.dict_to_csv(earnings, '../output/earnings.csv')


if __name__ == '__main__':
    main()
