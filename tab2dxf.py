from dxfwrite import DXFEngine as dxf
import pandas as pd
import numpy as np

rid=pd.read_csv('survey.csv')
k=[]
for i in rid.keys():
    k.append(i)
l=len(rid[k[0]])


drawing = dxf.drawing('survey.dxf')
lp=drawing.add_layer('Points')
lp['color']=7
lc=drawing.add_layer('Codes')
lc['color']=7
lc.off()
ln=drawing.add_layer('Numbers')
ln['color']=7
ln.off()
lco=drawing.add_layer('Elevations')
lco['color']=7


for j in range(0,l):
    point = dxf.point((2.0, 2.0))
    point['layer']='Points'
    point['thickness']=7
    point['point']=(rid[k[2]][j],rid[k[1]][j],rid[k[3]][j])
    drawing.add(point)

    text = dxf.text(rid[k[0]][j], insert=(rid[k[2]][j],rid[k[1]][j],rid[k[3]][j]), height=1)
    text['layer']='Numbers'
    drawing.add(text)

    code = dxf.text(rid[k[4]][j], insert=(rid[k[2]][j],rid[k[1]][j],rid[k[3]][j]), height=1)
    code['layer']='Codes'
    drawing.add(code)

    elevation = dxf.text(rid[k[3]][j], insert=(rid[k[2]][j],rid[k[1]][j],rid[k[3]][j]), height=1)
    elevation['layer']='Elevations'
    drawing.add(elevation)
drawing.save()
