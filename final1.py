# Name: Ruoyu Li
# Andrew ID: ruoyuli

import pandas as pd
import re

pd.set_option('display.expand_frame_repr', False)

# References:
#   https://docs.bokeh.org/en/2.4.3/docs/gallery/pie_chart.html

# For the 2020-2021 data to sort out: 
# 1. dataframe for different genres sorting;
# 2. dictionary of data for each song 
#       {'Song Name': {'Highest Charting Position': x, 
#       'Number of Times Charted': y, 'Streams': z, 'Artist': m, 
#       'Artist Followers': n, 'Genre': u, 'Popularity': v}
#       -- all values are strings!!!
# uses/prompts:
# 1. pie chart of different genres
# 2. prompt: song name => song information
# 3. prompt: two song name => info comparison dataframe
year_data = pd.read_csv('spotify_dataset.csv', index_col=0)
year_data.drop(['Week of Highest Charting', 'Song ID', 'Release Date', \
                'Weeks Charted', 'Danceability', 'Energy', 'Loudness', \
                'Speechiness', 'Acousticness', 'Liveness', 'Tempo', \
                'Duration (ms)', 'Valence', 'Chord'], axis=1, inplace=True)

# find "pop" in Genre
def isPop(piece):
    newList = piece[2:-2].split("', '")
    for row in newList:
        if re.search(r'pop', row) != None:
            return True
    return False

# find "hip hop" in Genre
def isHipHop(piece):
    newList = piece[2:-2].split("', '")
    for row in newList:
        if re.search(r'hip hop', row) != None:
            return True
    return False

# find "rap" in Genre
def isRap(piece):
    newList = piece[2:-2].split("', '")
    for row in newList:
        if re.search(r'(^rap)|( rap)', row) != None:
            return True
    return False

# find "trap" in Genre
def isTrap(piece):
    newList = piece[2:-2].split("', '")
    for row in newList:
        if re.search(r'(^trap)|( trap)', row) != None:
            return True
    return False

# find "k-pop" in Genre
def isKPop(piece):
    newList = piece[2:-2].split("', '")
    for row in newList:
        if re.search(r'(^k-pop)|( k-pop)', row) != None:
            return True
    return False

# find "r&b" in Genre
def isRNB(piece):
    newList = piece[2:-2].split("', '")
    for row in newList:
        if re.search(r'r&b', row) != None:
            return True
    return False

# find "latin" in Genre
def isLatin(piece):
    newList = piece[2:-2].split("', '")
    for row in newList:
        if re.search(r'latin', row) != None:
            return True
    return False

# find "reggaeton" in Genre
def isRegg(piece):
    newList = piece[2:-2].split("', '")
    for row in newList:
        if re.search(r'reggaeton', row) != None:
            return True
    return False

# find "house" in Genre
def isHouse(piece):
    newList = piece[2:-2].split("', '")
    for row in newList:
        if re.search(r'house', row) != None:
            return True
    return False

# find "dance" in Genre
def isDance(piece):
    newList = piece[2:-2].split("', '")
    for row in newList:
        if re.search(r'dance', row) != None:
            return True
    return False

# find "edm" in Genre
def isEDM(piece):
    newList = piece[2:-2].split("', '")
    for row in newList:
        if re.search(r'edm', row) != None:
            return True
    return False

# find "indie" in Genre
def isIndie(piece):
    newList = piece[2:-2].split("', '")
    for row in newList:
        if re.search(r'indie', row) != None:
            return True
    return False

# find "punk" in Genre
def isPunk(piece):
    newList = piece[2:-2].split("', '")
    for row in newList:
        if re.search(r'punk', row) != None:
            return True
    return False

# find other genres in Genre
def isOther(piece):
    if (isPop(piece) == False and isHipHop(piece) == False and 
        isRap(piece) == False and isTrap(piece) == False and
        isKPop(piece) == False and isRNB(piece) == False and
        isLatin(piece) == False and isRegg(piece) == False and
        isHouse(piece) == False and isDance(piece) == False and
        isEDM(piece) == False and isIndie(piece) == False and
        isPunk(piece) == False):
        return True
    return False

year_pop = year_data.loc[year_data['Genre'].apply(isPop)==True]
year_pop_num = year_pop['Song Name'].count()
popList = year_pop['Song Name'].values.tolist()

year_hiphop = year_data.loc[year_data['Genre'].apply(isHipHop)==True]
year_hiphop_num = year_hiphop['Song Name'].count()
hiphopList = year_hiphop['Song Name'].values.tolist()

year_rap = year_data.loc[year_data['Genre'].apply(isRap)==True]
year_rap_num = year_rap['Song Name'].count()
rapList = year_rap['Song Name'].values.tolist()

year_trap = year_data.loc[year_data['Genre'].apply(isTrap)==True]
year_trap_num = year_trap['Song Name'].count()
trapList = year_trap['Song Name'].values.tolist()

year_kpop = year_data.loc[year_data['Genre'].apply(isKPop)==True]
year_kpop_num = year_kpop['Song Name'].count()
kpopList = year_kpop['Song Name'].values.tolist()

year_rnb = year_data.loc[year_data['Genre'].apply(isRNB)==True]
year_rnb_num = year_rnb['Song Name'].count()
rnbList = year_rnb['Song Name'].values.tolist()

year_latin = year_data.loc[year_data['Genre'].apply(isLatin)==True]
year_latin_num = year_latin['Song Name'].count()
latinList = year_latin['Song Name'].values.tolist()

year_regg = year_data.loc[year_data['Genre'].apply(isRegg)==True]
year_regg_num = year_regg['Song Name'].count()
reggList = year_regg['Song Name'].values.tolist()

year_house = year_data.loc[year_data['Genre'].apply(isHouse)==True]
year_house_num = year_house['Song Name'].count()
houseList = year_house['Song Name'].values.tolist()

year_dance = year_data.loc[year_data['Genre'].apply(isDance)==True]
year_dance_num = year_dance['Song Name'].count()
danceList = year_dance['Song Name'].values.tolist()

year_edm = year_data.loc[year_data['Genre'].apply(isEDM)==True]
year_edm_num = year_edm['Song Name'].count()
edmList = year_edm['Song Name'].values.tolist()

year_indie = year_data.loc[year_data['Genre'].apply(isIndie)==True]
year_indie_num = year_indie['Song Name'].count()
indieList = year_indie['Song Name'].values.tolist()

year_punk = year_data.loc[year_data['Genre'].apply(isPunk)==True]
year_punk_num = year_punk['Song Name'].count()
punkList = year_punk['Song Name'].values.tolist()

year_other = year_data.loc[year_data['Genre'].apply(isOther)==True]
year_other_num = year_other['Song Name'].count()
otherList = year_other['Song Name'].values.tolist()

genreDict = {
    'Pop': year_pop_num,
    'Hip Hop': year_hiphop_num,
    'Rap': year_rap_num,
    'Trap': year_trap_num,
    'K-Pop': year_kpop_num,
    'R&B': year_rnb_num,
    'Latin': year_latin_num,
    'Reggaeton': year_regg_num,
    'House': year_house_num,
    'Dance': year_dance_num,
    'EDM': year_edm_num,
    'Indie': year_indie_num,
    'Punk': year_punk_num,
    'Other': year_other_num
}

