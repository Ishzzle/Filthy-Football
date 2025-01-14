import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
import time

#List of seasons
seasons = [str(season) for season in range(2010,2025)]
#Making it 2025 so it is inclusive of 2024. Update with each season

team_tags = ['crd','atl','rav','buf','car','chi','cin','cle','dal','den','det','gnb','htx',
            'clt','jax','kan','sdg','ram','rai','mia','min','nwe','nor','nyg','nyj','phi',
            'pit','sea','sfo','tam','oti','was']

#Data frame for NFL scores
nfl_dataframe = pd.DataFrame()

for season in seasons:
    for team in team_tags:
        url = 'https://www.pro-football-reference.com/teams/'+team+'/'+season+'/gamelog/'
        print(url)
