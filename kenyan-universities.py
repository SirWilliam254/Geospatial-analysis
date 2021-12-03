# important libraries
import pandas as pd
import geopandas as gpd
import numpy as np
import math
import folium 
from folium import Marker
from folium.plugins import MarkerCluster
# function to produce an Iframe object
def embed_map(m, file_name):
    from IPython.display import IFrame
    m.save(file_name)
    return IFrame(file_name, width='100%', height='500px')


# Reading in the data  
universities = pd.read_csv("~/ken_un.csv")
universities.head()

## Creating a base map
m_2 = folium.Map(location=[-1.18064, 36.93100], zoom_start=13)

# Adding a marker for each university
for idx, row in universities.iterrows():
    Marker([row['lat'], row['lon']], popup=row['name']).add_to(m_2)


# Show the map
embed_map(m_2, 'uni.html')
