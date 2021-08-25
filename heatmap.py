path = '/home/newmar/Downloads/Curso_PyQGIS/interpolacao/inter.gpkg'
layer = iface.addVectorLayer(path, "interpolar", "ogr")

fields = []
for field in layer.fields():
    fields.append(field.name())
print(fields)

count = 0
for field in fields:
   if count >= 5:
        layer = iface.addVectorLayer(path, f"{field}", "ogr")
        heatmap = QgsHeatmapRenderer()
        heatmap.setWeightExpression(f"{field}")
        ramp = QgsStyle().defaultStyle().colorRamp('Reds')
        heatmap.setColorRamp(ramp)
        heatmap.setRadius(20)
        layer.setRenderer(heatmap)
        layer.triggerRepaint()
   count += 1 
