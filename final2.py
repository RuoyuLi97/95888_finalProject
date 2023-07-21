# Name: Ruoyu Li
# Andrew ID: ruoyuli

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

pd.set_option('display.expand_frame_repr', False)

# For the web scraping of weekly charts of top songs to sort out:
#   1. Weekly Top Songs Global
#   2. Weekly Top Songs Australia
#   3. Weekly Top Songs Canada
#   4. Weekly Top Songs France
#   5. Weekly Top Songs Germany
#   6. Weekly Top Songs Hong Kong
#   7. Weekly Top Songs India
#   8. Weekly Top Songs Japan
#   9. Weekly Top Songs South Africa
#   10. Weekly Top Songs South Korea
#   11. Weekly Top Songs UK
#   12. Weekly Top Songs USA
# uses/prompts: 
#   location -- weekly top songs

# Global
urlGlobal = 'https://kworb.net/spotify/country/global_weekly.html'
# Australia
urlAu = 'https://kworb.net/spotify/country/au_weekly.html'
# Canada
urlCa = 'https://kworb.net/spotify/country/ca_weekly.html'
# France
urlFr = 'https://kworb.net/spotify/country/fr_weekly.html'
# Germany
urlGe = 'https://kworb.net/spotify/country/de_weekly.html'
# Hong Kong
urlHk = 'https://kworb.net/spotify/country/hk_weekly.html'
# India
urlIn = 'https://kworb.net/spotify/country/in_weekly.html'
# Japan
urlJp = 'https://kworb.net/spotify/country/jp_weekly.html'
# South Africa
urlSa = 'https://kworb.net/spotify/country/za_weekly.html'
# South Korea
urlSk = 'https://kworb.net/spotify/country/kr_weekly.html'
# UK
urlUk = 'https://kworb.net/spotify/country/gb_weekly.html'
# USA
urlUs = 'https://kworb.net/spotify/country/us_weekly.html'

# get infomation list from every row of table
def getInfo(rows):
    infoData = list()
    for row in rows:
        infoRow = list()
        infoList = row.find_all('td')
        ranking = int(infoList[0].get_text())
        infoRow.append(ranking)
        songInfo = infoList[2].find_all('a')
        songName = songInfo[1].get_text()
        infoRow.append(songName)
        if (len(songInfo) == 2):
            artist = songInfo[0].get_text()       
        else:
            artist = songInfo[0].get_text() + ',' + songInfo[2].get_text()
        infoRow.append(artist)
        stream = infoList[6].get_text()
        stream = int(re.sub(",", "", stream))
        infoRow.append(stream)
        infoData.append(infoRow)
    return infoData

pageGlobal = requests.get(urlGlobal)
soupGlobal = BeautifulSoup(pageGlobal.content, 'html.parser')
tableGlobal = soupGlobal.find('tbody')
rowsGlobal = tableGlobal.find_all('tr')
infoGlobalData = getInfo(rowsGlobal)
rankingGlobalDF = pd.DataFrame(infoGlobalData, 
                         columns=['Ranking', 'Song Name', 
                                  'Artists', 'Streams']).set_index('Ranking')

pageAu = requests.get(urlAu)
soupAu = BeautifulSoup(pageAu.content, 'html.parser')
tableAu = soupAu.find('tbody')
rowsAu = tableAu.find_all('tr')
infoAuData = getInfo(rowsAu)
rankingAuDF = pd.DataFrame(infoAuData, 
                         columns=['Ranking', 'Song Name', 
                                  'Artists', 'Streams']).set_index('Ranking')

pageCa = requests.get(urlCa)
soupCa = BeautifulSoup(pageCa.content, 'html.parser')
tableCa = soupCa.find('tbody')
rowsCa = tableCa.find_all('tr')
infoCaData = getInfo(rowsCa)
rankingCaDF = pd.DataFrame(infoCaData, 
                         columns=['Ranking', 'Song Name', 
                                  'Artists', 'Streams']).set_index('Ranking')

pageFr = requests.get(urlFr)
soupFr = BeautifulSoup(pageFr.content, 'html.parser')
tableFr = soupFr.find('tbody')
rowsFr = tableFr.find_all('tr')
infoFrData = getInfo(rowsFr)
rankingFrDF = pd.DataFrame(infoFrData, 
                         columns=['Ranking', 'Song Name', 
                                  'Artists', 'Streams']).set_index('Ranking')

pageGe = requests.get(urlGe)
soupGe = BeautifulSoup(pageGe.content, 'html.parser')
tableGe = soupGe.find('tbody')
rowsGe = tableGe.find_all('tr')
infoGeData = getInfo(rowsGe)
rankingGeDF = pd.DataFrame(infoGeData, 
                         columns=['Ranking', 'Song Name', 
                                  'Artists', 'Streams']).set_index('Ranking')

pageHk = requests.get(urlHk)
soupHk = BeautifulSoup(pageHk.content, 'html.parser')
tableHk = soupHk.find('tbody')
rowsHk = tableHk.find_all('tr')
infoHkData = getInfo(rowsHk)
rankingHkDF = pd.DataFrame(infoHkData, 
                         columns=['Ranking', 'Song Name', 
                                  'Artists', 'Streams']).set_index('Ranking')

pageIn = requests.get(urlIn)
soupIn = BeautifulSoup(pageIn.content, 'html.parser')
tableIn = soupIn.find('tbody')
rowsIn = tableIn.find_all('tr')
infoInData = getInfo(rowsIn)
rankingInDF = pd.DataFrame(infoInData, 
                         columns=['Ranking', 'Song Name', 
                                  'Artists', 'Streams']).set_index('Ranking')

pageJp = requests.get(urlJp)
soupJp = BeautifulSoup(pageJp.content, 'html.parser')
tableJp = soupJp.find('tbody')
rowsJp = tableJp.find_all('tr')
infoJpData = getInfo(rowsJp)
rankingJpDF = pd.DataFrame(infoJpData, 
                         columns=['Ranking', 'Song Name', 
                                  'Artists', 'Streams']).set_index('Ranking')

pageSa = requests.get(urlSa)
soupSa = BeautifulSoup(pageSa.content, 'html.parser')
tableSa = soupSa.find('tbody')
rowsSa = tableSa.find_all('tr')
infoSaData = getInfo(rowsSa)
rankingSaDF = pd.DataFrame(infoSaData, 
                         columns=['Ranking', 'Song Name', 
                                  'Artists', 'Streams']).set_index('Ranking')

pageSk = requests.get(urlSk)
soupSk = BeautifulSoup(pageSk.content, 'html.parser')
tableSk = soupSk.find('tbody')
rowsSk = tableSk.find_all('tr')
infoSkData = getInfo(rowsSk)
rankingSkDF = pd.DataFrame(infoSkData, 
                         columns=['Ranking', 'Song Name', 
                                  'Artists', 'Streams']).set_index('Ranking')

pageUk = requests.get(urlUk)
soupUk = BeautifulSoup(pageUk.content, 'html.parser')
tableUk = soupUk.find('tbody')
rowsUk = tableUk.find_all('tr')
infoUkData = getInfo(rowsUk)
rankingUkDF = pd.DataFrame(infoUkData, 
                         columns=['Ranking', 'Song Name', 
                                  'Artists', 'Streams']).set_index('Ranking')

pageUs = requests.get(urlUs)
soupUs = BeautifulSoup(pageUs.content, 'html.parser')
tableUs = soupUs.find('tbody')
rowsUs = tableUs.find_all('tr')
infoUsData = getInfo(rowsUs)
rankingUsDF = pd.DataFrame(infoUsData, 
                         columns=['Ranking', 'Song Name', 
                                  'Artists', 'Streams']).set_index('Ranking')