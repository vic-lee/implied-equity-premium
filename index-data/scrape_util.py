from bs4 import BeautifulSoup
from urllib import request as re
import csv


def soup_maker(url):
    content = re.urlopen(url).read()
    soup = BeautifulSoup(content, 'html.parser')
    return soup


def dict_to_csv(dict, filename):
    keys = dict.keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerow(dict)