names = [layer.name() for layer in QgsProject.instance().mapLayers().values()]
for i in names:
    #print(i)
    layer_canvas = i.split('—')[1].strip()
    processing.run("gdal:rasterize", 
    {'INPUT':f'/home/newmar/Downloads/testezip/final/car.gpkg|layername={layer_canvas}|geometrytype=Polygon',
    'FIELD':'','BURN':1,'USE_Z':False,'UNITS':1,'WIDTH':8e-05,'HEIGHT':8e-05,
    'EXTENT':'-54.703192342,-48.030792342,-26.804172401,-22.461772401 [EPSG:4326]',
    'NODATA':0,'OPTIONS':'COMPRESS=LZW|PREDICTOR=2|ZLEVEL=9','DATA_TYPE':0,'INIT':None,
    'INVERT':False,'EXTRA':'','OUTPUT':f'/home/newmar/Downloads/testezip/output/rasters/{layer_canvas}.tif'})