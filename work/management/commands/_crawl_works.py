from bs4 import BeautifulSoup
import requests
import re


def url(lastname):
    return 'https://www.wga.hu/cgi-bin/search.cgi?author={}&time=any&school=any&form=any&type=any&title=&comment=&location=&from=0&max=1000&format=5'.format(lastname)


class Piece:

    def __init__(self, image, name, info, start_year, finish_year, location):
        self.image = image
        self.name = name
        self.info = info
        self.start_year = start_year
        self.finish_year = finish_year
        self.location = location


def remove_all_but_numbers(text):
    return re.sub('[^0-9]', "", text)


def extract_year(text):
    start = None
    finish = None
    if '-' in text:
        start, finish = text.split('-')
        start = remove_all_but_numbers(start)
        finish = remove_all_but_numbers(finish)
        if len(finish) == 2:
            finish = start[:2]+finish
    else:
        finish = remove_all_but_numbers(text)
    if start:
        start = int(start)
    else:
        start = None
    if finish:
        finish = int(finish)
    else:
        finish = None
    return [start, finish]


def get_works(last_name):

    works = []
    req = requests.get(url(last_name))
    soup = BeautifulSoup(req.text, 'html.parser')
    center = soup.findAll('center')[1]
    table = center.find('table')
    if table:
        trs = table.findAll('tr', recursive=False)[1:]
        for tr in trs:
            image, info = tr.findAll('td', recursive=False)[:2]
            image = 'https://www.wga.hu'+image.find('a')['href']
            info = info.get_text().strip()
            info = info.splitlines()
            try:
                name, year, info, location = info[1:-1]
            except:
                continue
            try:
                start_year, finish_year = extract_year(year)
            except:
                start_year = None
                finish_year = None
            piece = Piece(image, name, info, start_year, finish_year, location)
            works.append(piece)
    return works
