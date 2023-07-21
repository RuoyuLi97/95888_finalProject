# Name: Ruoyu Li
# Andrew ID: ruoyuli

import pandas as pd
from math import pi
from bokeh.palettes import Category20c
from bokeh.plotting import figure, show
from bokeh.transform import cumsum
import final1
import final2
import final3

pd.set_option('display.expand_frame_repr', False)

# References:
#   https://docs.bokeh.org/en/2.4.3/docs/gallery/pie_chart.html
#   https://www.youtube.com/watch?v=WAmEZBEeNmg
#   https://developer.spotify.com/documentation/web-api/tutorials

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

genreDF = pd.Series(final1.genreDict).reset_index(name='Count').rename(columns={'index': 'Genre'})
genreDF['angle'] = genreDF['Count']/genreDF['Count'].sum() * 2*pi
genreDF['color'] = Category20c[len(final1.genreDict)]

genrePlot = figure(height=400, title="Pie Chart of Genres", toolbar_location=None,
           tools="hover", tooltips="@Genre: @Count", x_range=(-0.5, 1.0))

genrePlot.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='Genre', source=genreDF)

genrePlot.axis.axis_label = None
genrePlot.axis.visible = False
genrePlot.grid.grid_line_color = None


searchDF = final1.year_data.copy()
searchDF.set_index('Song Name', drop=True, inplace=True)
searchDict = searchDF.to_dict(orient='index')
# {'Song Name': {'Highest Charting Position': x, 
#       'Number of Times Charted': y, 'Streams': z, 'Artist': m, 
#       'Artist Followers': n, 'Genre': u, 'Popularity': v}

# get song info from searchDict
def getSongInfo(song):
    infoDict = searchDict[song]
    infoList = list()
    for key in infoDict:
        infoList.append(infoDict[key])
    return infoList

# create a dataframe comparing two songs infomation
def twoSongComparison(songA, songB):
    infoListA = getSongInfo(songA)
    infoListB = getSongInfo(songB)
    dataDict = dict()
    dataDict[songA] = infoListA
    dataDict[songB] = infoListB
    compareDF = pd.DataFrame(data=dataDict, index=['Highest Charting Position', 
                                                   'Number of Times Charted',
                                                   'Streams', 'Artist', 
                                                   'Artist Followers', 'Genre',
                                                   'Popularity'])
    return compareDF

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
rankingGlobalDF = final2.rankingGlobalDF
rankingAuDF = final2.rankingAuDF
rankingCaDF = final2.rankingCaDF
rankingFrDF = final2.rankingFrDF
rankingGeDF = final2.rankingGeDF
rankingHkDF = final2.rankingHkDF
rankingInDF = final2.rankingInDF
rankingJpDF = final2.rankingJpDF
rankingSaDF = final2.rankingSaDF
rankingSkDF = final2.rankingSkDF
rankingUkDF = final2.rankingUkDF
rankingUsDF = final2.rankingUsDF
rankingDict = {
    'Global': rankingGlobalDF,
    'Australia': rankingAuDF,
    'Canada': rankingCaDF,
    'France': rankingFrDF,
    'Germany': rankingGeDF,
    'Hong Kong': rankingHkDF,
    'India': rankingInDF,
    'South Africa': rankingSaDF,
    'South Korea': rankingSkDF,
    'Uk': rankingUkDF,
    'Usa': rankingUsDF}

# For retrieving structured data using the API of "Taylor Swift - 
# The Eras Tour Setlist" to sort out:
#   dataframe groupby album
# uses/prompts: 
#   dataframe of playlist
#   pie chat of albums that containing songs performed on The Eras Tour

# Client ID: f69b3352714d4147b173c65ece84229b
# Client Secret: 7904bb22bba44ba09ba6a27cddbefbac
playlistDF = final3.playListDF


print('\n')
print('Welcome to use Music Analysis to see what is trendy recently!\n')
print('-------------------------------------------------------------\n')
print('Based on the data from Spotify, you can get:\n')
print('1. Song Information from Spotify Top 200 Charts (2020-2021)\n')
print('2. Genre Analysis from Spotify Top 200 Charts (2020-2021)\n')
print('3. Song Popularity Comparison from Spotify Top 200 Charts (2020-2021)\n')
print('4. Latest Weekly Top 10 Songs in different countries\n')
print('Moreover, there is a special for Taylor Swift fans - \n')
print('5. Playlist of The Eras Tour\n')
print('6. Song Analysis which performed on the Eras Tour\n')
print("Now, let's start!\n")
print('-------------------------------------------------------------\n')

while True:
    num = input('Enter the serial number above or DONE to quit:')
    if (num.upper() == 'DONE'):
        print('Thank you for using!\n')
        break
    elif (not num.isdigit() or int(num) <= 0 or int(num) >= 7):
        print('Invalid Input!\n')
        print('-------------------------------------------------------------\n')
    else:
        if (int(num) == 1):
            while True:
                songName = input('Enter a song name to see the information in the Spotify Top 200 Charts (2020-2021):')
                if (songName.title() not in searchDict):
                    print('Oops! Seems this song is either wrongly spelled or not in the chart!')
                else:
                    break
            print('%s: \n' % songName.title())
            items = searchDict[songName.title()]
            for item in items:
                print('%s: ' % item, end='')
                print(items[item])
                print('\n')

        elif (int(num) == 2):
            print('Here is the pie chart of genre analysis of Spotify Top 200 Charts (2020-2021)\n')
            print('Watch out! It will pop up in the browser!\n')
            show(genrePlot)

        elif (int(num) == 3):
            print("Enter two songs' names to compare!\n")
            while True:
                songA = input('Enter the first name:')
                if (songA.title() not in searchDict):
                    print('Oops! Seems this song is either wrongly spelled or not in the chart!')
                else:
                    break
            while True:
                songB = input('Enter the second name:')
                if (songB.title() not in searchDict):
                    print('Oops! Seems this song is either wrongly spelled or not in the chart!')
                else:
                    break
            print('Here is the comparison result between %s and %s: \n' % (songA.title(), songB.title()))
            print(twoSongComparison(songA.title(), songB.title()))
        
        elif (int(num) == 4):
            print("Here are the countries' data available: \n")
            print('- Global\n')
            print('- Australia\n')
            print('- Canada\n')
            print('- France\n')
            print('- Germany\n')
            print('- Hong Kong\n')
            print('- India\n')
            print('- Japan\n')
            print('- South Africa\n')
            print('- South Korea\n')
            print('- UK\n')
            print('- USA\n')
            while True:
                country = input('Enter a country of which you would like to know the latest weekly top 10 songs:')
                if (country.title() not in rankingDict):
                    print('Invalid Input!\n')
                else:
                    break
            ranking = rankingDict[country.title()]
            print(ranking.iloc[:10])
        
        elif (int(num) == 5):
            print('Here is the playlist of The Eras Tour:\n')
            print(playlistDF.sort_values(by='Popularity', ascending=False))
            print('\n')
        
        else:
            playlistDFCopy = playlistDF.copy()
            orderedPlaylistDF = playlistDFCopy.groupby(by=['Album']).count().sort_values(by='Song Name', ascending=False)
            print("The Song Analysis reflects the popularity of Taylor's albums: \n")
            print(orderedPlaylistDF)
            print('\n')
        
        print('-------------------------------------------------------------\n')


