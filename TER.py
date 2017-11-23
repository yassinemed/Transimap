from PyQt4.QtCore import *
from osgeo import gdal
from osgeo.gdalconst import *

#driver = gdal.GetDriverByName('GTiff')
#driver.Register()

rlayer = "F:\\MASTER GEOM\\MasterGeomatique_data\\PLEIADES\\PLEIADES_20130415_COLNAT.TIF"
rlayer = gdal.Open(rlayer, GA_ReadOnly)
provider = QgsVectorLayer("F:\essai1.shp", 'essai', 'ogr')
extent = provider.extent()

#QgsMapLayerRegistry.instance().addMapLayer(provider)
#QgsMapLayerRegistry.instance().addMapLayer(rlayer)

band_list = []
cols = rlayer.RasterXSize
cols1 = rlayer.RasterXSize/10
rows = rlayer.RasterYSize
rows1 = rlayer.RasterXSize/10
print(cols1)
for i in range(rlayer.RasterCount):
    bands =rlayer.GetRasterBand(i+1)
    data = bands.ReadAsArray()
    for data in  range(cols1) :
        for data in range(rows1):
            band_list.append(data)
            percentTransparent = 100 
            print (band_list[0])
   

        