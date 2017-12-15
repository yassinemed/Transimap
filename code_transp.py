from PyQt4.QtCore import *
from osgeo import gdal, ogr
from osgeo.gdalconst import *
import numpy as np

iface = qgis.utils.iface

layers = iface.legendInterface().layers()
raster = gdal.Open("F:\\MASTER GEOM\\MasterGeomatique_data\\PLEIADES\\PLEIADES_20130415_COLNAT.TIF")
print(raster)

transform = raster.GetGeoTransform()
xOrigin = transform[0]
yOrigin = transform[3]
pixelWidth = transform[1]
pixelHeight = transform[5]
print xOrigin, yOrigin

     
shp = ogr.Open("F:\essai.shp")
lyr = shp.GetLayer()
feat = lyr.GetNextFeature()
geom = feat.GetGeometryRef()
  
if (geom.GetGeometryName() == 'POLYGON'):
    ring = geom.GetGeometryRef(0)
    numpoints = ring.GetPointCount()
    pointsX = []; pointsY = []
    for p in range(numpoints):
                lon, lat, z = ring.GetPoint(p)
                pointsX.append(lon)
                pointsY.append(lat)
                #print (pointsX)
xmin = min(pointsX)
xmax = max(pointsX)
ymin = min(pointsY)
ymax = max(pointsY)
print xmin, ymin
print xmax, ymax  
 # Specify offset and rows and columns to read
xoff = int((xmin - xOrigin)/pixelWidth)
yoff = int((yOrigin - ymax)/pixelWidth)
xcount = int((xmax - xmin)/pixelWidth)+1
ycount = int((ymax - ymin)/pixelWidth)+1
print xoff, yoff
print xcount, ycount

bandList = []
# lecture des bandes uniquement pour la region d' interet
for i in range(raster.RasterCount):
	band = raster.GetRasterBand(i+1)
	data = band.ReadAsArray(xoff, yoff, xcount, ycount)
	bandList.append(data)
#   print (np.max(bandList))
#for i in range(0, xcount):
#    for j in range(0, ycount):
#calcul du NDVI
##        ndvi = (float(bandList [1][ j ][ i ]) - float(bandList [2][ j ][ i ]) ) / ( float (bandList [1][ j ][ i ]) + float(bandList [2][ j ][ i ]) )
#        s = str( i ) + ' ' + str(j) + ' : ' + str(ndvi)
#        print s
print 'Start'
active_layer = raster
raster_transparency  = active_layer.renderer().rasterTransparency()
ltr = QgsRasterTransparency.TransparentThreeValuePixel()
tr_list = []
ltr.min = np.min(bandList)
ltr.max = np.max(bandList)
ltr.percentTransparent = 100  
tr_list.append(ltr)  
active_layer.renderer().rasterTransparency().setTransparentThreeValuePixelList(tr_list)
active_layer.triggerRepaint() 
print 'Finish'
QgsMapLayerRegistry.instance().addMapLayer(raster)
# Message d'erreur : AttributeError: 'Dataset' object has no attribute 'renderer'