from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('iran_cities.csv')

m = Basemap(width=5000000,height=4900000,projection='lcc',
            resolution='c',lat_1=25.,lat_2=40.,lat_0=44.,lon_0=63.)

m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='coral',lake_color='aqua')
parallels = np.arange(0.,81,10.)
m.drawparallels(parallels,labels=[False,True,True,False])
meridians = np.arange(10.,351.,10.)
m.drawmeridians(meridians,labels=[True,False,False,True])
lon = data["longitude"].values
lat = data["latitude"].values
city = data["name"].values
population = data["population"].values
scalar = []
for item in population:
   scalar.append(float(item)/100000)

xpt,ypt = m(lon,lat)
lonpt, latpt = m(xpt,ypt,inverse=True)
m.scatter(xpt,ypt,scalar,"blue",alpha=0.7)
plt.title("Scatter Plot of Population")
plt.show()



















