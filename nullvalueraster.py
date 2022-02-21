import os
from osgeo import gdal, gdal_array
import numpy as np

dir_path = 'INPUT_PATH'
out_dir = 'OUTPUT_PATH'


for root, directory, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.tif'):
            path = os.path.join(root,file)
            out_file = os.path.join(out_dir,file)
            raster = gdal.Open(path)
            array = raster.ReadAsArray()
            array = np.array(array, dtype=np.uint16)
            soma = array[0]+array[1]+array[2]
            mask = soma/soma
            raster_final = array * mask
            raster_final[np.where(np.isnan(raster_final))] = -1
            raster_final = np.array(raster_final,dtype=np.int16)
            #gdal_array.SaveArray(mask,out_path,"Gtiff",prototype=raster)
            gdal_array.SaveArray(raster_final,out_file,"Gtiff",prototype=raster)
            raster = None
