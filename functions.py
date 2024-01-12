
 # to download html code
import requests
from bs4 import BeautifulSoup # to navigate through the html code
import pandas as pd
import numpy as np
import re

def scrape_hot100():
    hot_songs_url = "https://www.billboard.com/charts/hot-100/"
    hot_songs_response = requests.get(hot_songs_url)
    hot_songs_soup = BeautifulSoup(hot_songs_response.text, 'html.parser')
    
    if hot_songs_response.status_code == 200:
        
        hot_songs_titles = [elem.get_text().replace("\n", "").replace("\t", "") for elem in hot_songs_soup.select("div  ul  li  ul  li  h3")]
        hot_songs_artists = [elem.parent.find_all("span")[0].get_text().replace("\n", "").replace("\t","") for elem in hot_songs_soup.select("div ul li ul li h3")]
        
        hot_songs_df = pd.DataFrame({'artist': hot_songs_artists, 'title': hot_songs_titles})
        hot_songs_df.to_csv("hot_100.csv", index=False)
        return hot_songs_df
