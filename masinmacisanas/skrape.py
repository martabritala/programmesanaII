import requests
import os
from bs4 import BeautifulSoup as bs
import csv
import time


URL = "https://www.ss.lv/lv/transport/cars/today-5/sell/"
LAPAS = "lapas/"
DATI = "dati/"

def saglaba(url, datne):
    rezultats = requests.get(url)
    print(rezultats.status_code)
    if rezultats.status_code == 200:
        with open(datne, 'w', encoding='utf-8') as fails:
            fails.write(rezultats.text)
    return

# saglaba(URL, LAPAS+"pirma.html")

def dabut_info(datne):
    dati = []
    with open(datne, "r", encoding="utf-8") as f:
        html = f.read()
    
    zupa = bs(html, 'html.parser')

    galvena_dala = zupa.find(id='page_main')

    tabulas = galvena_dala.find_all('table')

    rindas = tabulas[2].find_all('tr')
    for rinda in rindas[1:-1]: # Vai arī [1:] un tad jāizmanto 36-38 rinda
        lauki = rinda.find_all('td')
        # if len(lauki)<8:
        #     print('izlaist')
        #     continue
        auto = {}
        auto['sludinajuma_saite'] = lauki[1].find('a')['href']
        auto['bilde'] = lauki[1].find('img')['src']
        print(auto)
        dati.append(auto)
    return dati



print(dabut_info(LAPAS+"pirma.html"))


