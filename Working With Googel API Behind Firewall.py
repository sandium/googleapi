#!/usr/bin/env python
# coding: utf-8


#importing all required
import pandas as pd
import googlemaps
import pyodbc
import os
os.environ['http_proxy'] = "http://userid:password@proxy_IP:Proxy_Port" 
os.environ['https_proxy'] = "https://userid:password@proxy_IP:Proxy_Port"


server = 'database Host name or IP' 
database = 'database name' 
username = 'db user' 
password = 'db password' 



#GET DATA INTO DATA FROM FROM SQL SERVER
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = conn.cursor()

df = pd.read_sql_query("SELECT Clientcode,address  FROM TEMP_CUSTOMER",conn)



#df


#setting up google key for coordinates
gmaps = googlemaps.Client(key = "your google api key",)
df["Latitude"] = None
df["Longitude"] = None



for i in range(0, len(df)):
    geocode_result = gmaps.geocode(df.iat[i,1])
    try:
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lon = geocode_result[0]["geometry"]["location"]["lng"]
        df.iat[i, df.columns.get_loc("Latitude")] = lat
        df.iat[i, df.columns.get_loc("Longitude")] = lon
        Latitude=df.iat[i, df.columns.get_loc("Latitude")]
        Longitude=df.iat[i, df.columns.get_loc("Longitude")]
        ClientID=df.iat[i, df.columns.get_loc("Clientcode")]
        print(Latitude,Longitude)
        UPDATE = ("UPDATE TEMP_CUSTOMER SET LATITUDE =?,LONGITUDE =? WHERE Clientcode=?")
        VALUES = (Latitude,Longitude,ClientID)
        conn.execute(UPDATE,VALUES)
        conn.commit()
    except:
        print("I am here!!")

