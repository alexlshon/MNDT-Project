#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:43:56 2019

@author: xiaohezhang
"""

# Import libaries
import pandas as pd
import requests
import time
import datetime
import progressbar


import twitter
api = twitter.Api(consumer_key='YfkfmWvtZAz7SS9GHRZzpleNc',
                  consumer_secret='O9sQl3eHtq6EMbKh5vsvLwaaiLXRKNVhfd50mb7yEa83LX6NPK',
                  access_token_key='2453541001-sJHmhzs9LD7y37FIJTuQQDMXEhybFpIqTGuEkHG',
                  access_token_secret='VR0tUAq74JTW5bmkKtyPwdjBBOkVMAV0eKBL8pU2wmMAm')

#print(api.VerifyCredentials())

def create_table(x):
    result = {
        'created':[],
        'text':[],
        'location':[],
        'hashtags':[]
    }
    for i in range(len(x)):
        result['created'].append(pd.Timestamp(x[i].created_at_in_seconds, unit='s'))
        result['text'].append(x[i].text)
        result['location'].append(x[i].geo)
        result['hashtags'].append(x[i].hashtags)
    return pd.DataFrame(result, columns = ['created','text','location','hashtags'])

def get_data(term = None, since = None, until = None, geocode = None,):
    output = pd.DataFrame()
    for i in range(1):
        search = api.GetSearch(term, since = since, until = until, geocode = geocode, lang='en',count = 100)
        output = pd.concat([output, create_table(search)], axis = 0)
        time.sleep(3)
#         print(f'Fetching data {(i+1)*100}')
    return output


def reset_today():
    url = 'https://satepsanone.nesdis.noaa.gov/pub/FIRE/HMS/KML/'
    today = datetime.datetime.today().strftime('%Y%m%d')
    return requests.get(url+f'fire{today}.kml').content




#mapping(dfc,dfc.index[4])
def searchearthquake():
    url ="https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.csv"
    data = pd.read_csv(url)
    coordinates = []
    result = pd.DataFrame()
    for i in dfc.index:
        coordinates.append(f"{dfc.loc[i,'latitude']},{dfc.loc[i,'longitude']},10mi")
    bar = progressbar.ProgressBar(maxval=len(coordinates), widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    for j in range(len(coordinates)):
        dfj = get_data(geocode=coordinates[j])
        dfj['locationcoor'] = coordinates[j]
        result = pd.concat([result,dfj], axis = 0)
        bar.update(j+1)
    bar.finish()
    return result


result is testing set

