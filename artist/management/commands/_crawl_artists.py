import requests
from bs4 import BeautifulSoup
import re


class Artist:

    def __init__(self, last_name, first_name, born, died, period, nationality, profession):
        self.last_name = last_name
        self.first_name = first_name
        self.born = born
        self.died = died
        self.period = period
        self.nationality = nationality
        self.profession = profession

    def introduce(self):
        print(self.last_name, self.first_name, self.born, self.died,
              self.period, self.nationality, self.profession)


def extarct_name(text):
    # (see ...) 형식인 경우 see 뒤의 text를 가져옴
    if '(see' in text:
        text = text[text.index('(see')+4:text.index(')')]
    # first name이 없을 경우
    if ',' not in text:
        return [text.strip().lower().capitalize(), None]
    last_name, first_name = text.split(',')[:2]
    last_name = last_name.strip().lower().capitalize()
    first_name = first_name.strip()
    return [last_name, first_name]


def extract_year(text):
    # - 가 없을 경우 None 리턴 (정확하지 않으므로 표기하지 않음)
    if '-' not in text:
        return [None, None]
    count = text.count('-')
    if count > 1:
        text = text.replace('-', '', count-1)
    # () 제거
    born, died = text.split('-')
    # 숫자만 남기기
    born = re.sub('[^0-9]', "", born)
    died = re.sub('[^0-9]', "", died)
    if born == '' or died == '':
        return [None, None]
    born = int(born)
    died = int(died)
    return [born, died]


def get_artist(tr):
    info = tr.find_all('td', class_='ARTISTLIST')
    name, born_died, period, school = info

    last_name, first_name = extarct_name(name.get_text())

    born, died = extract_year(born_died.get_text())

    period = period.get_text().strip()

    school = school.get_text().split(' ')

    nationality = school[0].strip()

    profession = " ".join(list(
        filter(lambda x: (x != '' and '(' not in x and ')' not in x), school[1:])))

    return Artist(last_name, first_name, born, died, period, nationality, profession)


def get_all_artists():
    base_url = 'https://www.wga.hu/cgi-bin/artist.cgi?Profession=any&School=any&Period=any&Time-line=any&from=1&max=2000&Sort=Name&letter='
    artists = []
    for a in range(ord('a'), ord('z')):
        req = requests.get(base_url+chr(a))
        soup = BeautifulSoup(req.text, 'html.parser')
        div = soup.find('div', class_='PAGENUM')
        center = div.find('center').find('center')
        trs = center.find_all('tr')[1:]
        for tr in trs:
            artist = get_artist(tr)
            artists.append(artist)
    return artists


def get_certain_artists():
    base_url = 'https://www.wga.hu/cgi-bin/artist.cgi?Profession=any&School=any&Period=any&Time-line=any&from=150&max=50&Sort=Name&letter=l'
    artists = []
    req = requests.get(base_url)
    soup = BeautifulSoup(req.text, 'html.parser')
    div = soup.find('div', class_='PAGENUM')
    center = div.find('center').find('center')
    trs = center.find_all('tr')[1:]
    for tr in trs:
        artist = get_artist(tr)
        artists.append(artist)
    return artists
