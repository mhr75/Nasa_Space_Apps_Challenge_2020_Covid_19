import numpy as np
from netCDF4 import Dataset
#import matplotlib.pyplot as plt
#import cartopy.crs as ccrs
#import metpy


my_example_nc_file = 'MERRA2_400.tavgM_2d_aer_Nx.202004.nc4'
fh = Dataset(my_example_nc_file, mode='r')
#data = Dataset('MERRA2_400.tavgM_2d_aer_Nx.202004.nc4', mode='r')

print(fh)
lons = fh.variables['lon'][:]
lats = fh.variables['lat'][:]
tmax = fh.variables['time'][:]

tmax_units = fh.variables['time'].units


# lons = data.variables['lon'][:]
# lats = data.variables['lat'][:]
# T2M = data.variables['T2M'][:,:,:]
#
# T2M = T2M[0,:,:]

# Set the figure size, projection, and extent
# fig = plt.figure(figsize=(8,4))
# ax = plt.axes(projection=ccrs.Robinson())
# ax.set_global()
# ax.coastlines(resolution="110m",linewidth=1)
# ax.gridlines(linestyle='--',color='black')

# Set contour levels, then draw the plot and a colorbar
# clevs = np.arange(230,311,5)
# plt.contourf(lons, lats, T2M, clevs, transform=ccrs.PlateCarree(),cmap=plt.cm.jet)
# plt.title('MERRA-2 Air Temperature at 2m, January 2010', size=14)
# cb = plt.colorbar(ax=ax, orientation="vertical", pad=0.02, aspect=16, shrink=0.8)
# cb.set_label('K',size=12,rotation=0,labelpad=15)
# cb.ax.tick_params(labelsize=10)

# Save the plot as a PNG image

# fig.savefig('MERRA2_t2m.png', format='png', dpi=360)
#
fh.close()

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Get some parameters for the Stereographic Projection
lon_0 = lons.mean()
lat_0 = lats.mean()

m = Basemap(width=5000000,height=3500000,
            resolution='l',projection='stere',\
            lat_ts=40,lat_0=lat_0,lon_0=lon_0)

# Because our lon and lat variables are 1D,
# use meshgrid to create 2D arrays
# Not necessary if coordinates are already in 2D arrays.
lon, lat = np.meshgrid(lons, lats)
xi, yi = m(lon, lat)

# Plot Data
cs = m.pcolor(xi,yi,np.squeeze(tmax))

# Add Grid Lines
m.drawparallels(np.arange(-80., 81., 10.), labels=[1,0,0,0], fontsize=10)
m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)

# Add Coastlines, States, and Country Boundaries
m.drawcoastlines()
m.drawstates()
m.drawcountries()

# Add Colorbar
cbar = m.colorbar(cs, location='bottom', pad="10%")
cbar.set_label(tmax_units)

# Add Title
plt.title('DJF Maximum Temperature')

print(plt.show())