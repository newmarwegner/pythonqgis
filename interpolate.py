import qgis.analysis
import qgis.core

layer = qgis.utils.iface.activeLayer()
list_fields = []

for field in layer.fields():
    list_fields.append(field.name())
    
list_fields = list_fields[4:]
for field in list_fields:
    processing.run("grass7:v.surf.idw", 
                    {'input':'/home/newmar/Downloads/Dados_2019.shp',
                    'npoints':12,'power':2,'column':f'{field}',
                    '-n':False,'output':f'/home/newmar/Downloads/teste/' + f'{field}.tif',
                    'GRASS_REGION_PARAMETER':None,
                    'GRASS_REGION_CELLSIZE_PARAMETER':10,
                    'GRASS_RASTER_FORMAT_OPT':'',
                    'GRASS_RASTER_FORMAT_META':'',
                    'GRASS_SNAP_TOLERANCE_PARAMETER':-1,
                    'GRASS_MIN_AREA_PARAMETER':0.0001})