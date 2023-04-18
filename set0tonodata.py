layer = QgsProject.instance().mapLayersByName('risco')[0]
fs = layer.fields()
d = {e:0 if f.isNumeric() else '0' for e,f in enumerate(fs)}
with edit(layer):
    for row in layer.getFeatures():
        data = row.attributes()
        for i, val in enumerate(data):
            if val == NULL:
                data[i]=d[i]
        row.setAttributes(data)
        layer.updateFeature(row)