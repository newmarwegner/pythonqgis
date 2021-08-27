## Script to be use in PyQGIS to get shortest_paths between two vector layers.

## Step 01: Generating routes many to many
base_path = os.getcwd() + '/Downloads/shortest/originais/base_dados/'
output_folder = os.getcwd() + '/Downloads/shortest/originais/base_dados/linhas/'
path_roads = os.path.join(base_path,'roads_t.gpkg')
path_substacao = os.path.join(base_path,'substacao_geocodigo.gpkg')
path_inertes = os.path.join(base_path,'pontos_geocodigo.gpkg')
layer_roads = iface.addVectorLayer(path_roads, "roads", "OGR")
layer_substacao = iface.addVectorLayer(path_substacao, "substacao", "OGR")
layer_inertes = iface.addVectorLayer(path_inertes, "inertes", "OGR")

for coord_inerte in layer_inertes.getFeatures():
   for coor_est in layer_substacao.getFeatures():
        startx = coord_inerte.geometry().asPoint()[0]
        starty = coord_inerte.geometry().asPoint()[1]
        endx = coor_est.geometry().asPoint()[0]
        endy = coor_est.geometry().asPoint()[1]
        print(f"Gerando caminho da origem {coord_inerte.attributes()[0]} para destino {coor_est.attributes()[0]}")
        processing.run("qneat3:shortestpathpointtopoint", 
        {'INPUT':path_roads,
        'START_POINT':f"{startx},{starty}[EPSG:4674]",
        'END_POINT':f"{endx},{endy}[EPSG:4674]",
        'STRATEGY':0,
        'ENTRY_COST_CALCULATION_METHOD':0,
        'DIRECTION_FIELD':'',
        'VALUE_FORWARD':'',
        'VALUE_BACKWARD':'',
        'VALUE_BOTH':'',
        'DEFAULT_DIRECTION':2,
        'SPEED_FIELD':'',
        'DEFAULT_SPEED':5,
        'TOLERANCE':0,
        'OUTPUT':f"{output_folder}{coord_inerte.attributes()[0]}_{coor_est.attributes()[0]}.gpkg"})


## Step 02: Create a list of paths to be use in merge vector layers
path = '/home/newmar/Downloads/shortest/originais/base_dados/linhas'
out_path = '/home/newmar/Downloads/shortest/originais/base_dados'
lista = []
for root, directory, files in os.walk(path):
    for file in files:
        if file.endswith('.gpkg'):
            lista.append(os.path.join(path,file))

func = lambda x: x.split('/')[-1].split('_')[0]
temp = sorted(lista, key=func)

lista2 = [list(lista) for i, lista in groupby(temp, func)]

for lista in lista2:
    name = ponto[0].split('/')[-1].split('_')[0]
    name = name.zfill(3)
    processing.run("native:mergevectorlayers", 
    {'LAYERS':lista,
    'CRS':None,
    'OUTPUT':f'{out_path}/finais/{name}.gpkg'})


## Step 03: Create fields with a class (id of point) and measure lines
out_path = '/home/newmar/Downloads/shortest/originais/base_dados/finais'

vectors = []
for root, directory, files in os.walk(out_path):
    for file in files:
        if file.endswith('.gpkg'):
            vectors.append(os.path.join(out_path,file))

d = QgsDistanceArea()
d.setEllipsoid('WGS84')
for i in vectors:
    value = i.split('/')[-1][0:-5]
    layer = QgsVectorLayer(i, value,"ogr")
    layer.startEditing()
    layer.addAttribute(QgsField('classe',QVariant.Double))
    layer.addAttribute(QgsField('extensao',QVariant.Double))
    layer.commitChanges()

for i in vectors:
    value = i.split('/')[-1][0:-5]
    layer = QgsVectorLayer(i, value,"ogr")
    layer.startEditing()
    for feature in layer.getFeatures():
        id = feature.id()
        geom = feature.geometry()
        dist = d.measureLength(geom)
        layer.changeAttributeValue(id, 11,int(value))
        layer.changeAttributeValue(id, 12,dist)
        print (f'Camada {value} feature {id} e valor aplicado {result}')
    layer.commitChanges()
