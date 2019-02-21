from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import request as re
import csv


def soup_maker(url):
    """Returns a BeautifulSoup, given an url.
    This version utilizes urllib. 
    """
    content = re.urlopen(url).read()
    soup = BeautifulSoup(content, 'html.parser')
    return soup


def soup_maker_webdriver(url, headless=False):
    """Return a BeaultifulSoup object, given a url.
    This version utilizes selenium driver.
    """
    try:
        chrome_options = webdriver.ChromeOptions()
        if headless:
            chrome_options.add_argument('--headless')
        with webdriver.Chrome('_driver/chromedriver', chrome_options=chrome_options) as driver:
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
        return soup
    except Exception as e:
        print(e)
        return None


def dict_to_csv(dict, filename):
    """Write a dictionary to a new csv file, given a dict and a filename.
    Note that if a file named `filename` already exists, this function 
    will override that file without warning. 
    """
    keys = dict.keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerow(dict)
