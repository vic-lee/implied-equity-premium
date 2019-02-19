from bs4 import BeautifulSoup
from urllib import request as re
import csv


def soup_maker(url):
    content = re.urlopen(url).read()
    soup = BeautifulSoup(content, 'html.parser')
    return soup


def multpl_table_parser(url):
    contents = {}
    soup = soup_maker(url)
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
    earnings = multpl_table_parser("http://www.multpl.com/s-p-500-earnings/table")
    return earnings


def extract_annual_dividends():
    dvds = multpl_table_parser("http://www.multpl.com/s-p-500-dividend/table")
    return dvds


def dict_to_csv(dict, filename):
    keys = dict.keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerow(dict)


def main():
    dividends = extract_annual_dividends()
    print(dividends)

    earnings = extract_annual_earnings()
    print(earnings)

    dict_to_csv(dividends, 'dividends.csv')
    dict_to_csv(earnings, 'earnings.csv')


if __name__ == '__main__':
    main()
