import qgis.analysis
import qgis.core

layer = qgis.utils.iface.activeLayer()
features = layer.getFeatures()
count=0
for feature in features:
    geo = QgsGeometry.asPoint(feature.geometry())
    x = geo.x()
    y = geo.y()
    processing.run("grass7:r.water.outlet", 
    {'input':'/home/newmar/Downloads/tuto_basin/drainage.tif',
    'coordinates':f"{str(x)},{str(y)} [EPSG:31982]",
    'output':f"/home/newmar/Downloads/tuto_basin/basins/{count}.tif",
    'GRASS_REGION_PARAMETER':'183550.029300000,439466.883100000,7199816.088400000,7381693.524000000 [EPSG:31982]',
    'GRASS_REGION_CELLSIZE_PARAMETER':0,
    'GRASS_RASTER_FORMAT_OPT':'',
    'GRASS_RASTER_FORMAT_META':''})
    count+=1