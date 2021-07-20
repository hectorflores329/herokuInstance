from flask import Flask
import folium
import folium.plugins as plugins
import numpy as np
import pandas as pd
from flask import request
from datetime import datetime, timedelta
from folium.plugins import FloatImage
from folium.plugins import Draw
from folium.plugins import MiniMap

app = Flask(__name__)

@app.route('/')
# def mapa(codigo = '15'):
def mapa():

    codigo = request.args.get("codigo")
    codigo = str(codigo)

    comuna = request.args.get("comuna")
    comuna = str(comuna)

    cuenca = request.args.get("cuenca")
    cuenca = str(cuenca)

    # atlas = folium.raster_layers.WmsTileLayer(url = 'https://ide.dataintelligence-group.com/geoserver/chile/wms?', layers='chile:Regiones', name='test', fmt='image/png', attr='test', transparent=True, version='1.3.0')

    m = folium.Map(
        location=[-33.48621795345005, -70.66557950912359],
        zoom_start=5,
        min_zoom = 8,
        max_zoom = 30,
        control_scale=True
        # tiles = "openstreetmap"
        )

    codCuenca = "CQL_FILTER=COD_CUENCA=" + cuenca
    w = folium.WmsTileLayer(url = 'https://ide.dataintelligence-group.com/geoserver/glaciares_r14/wms?' + codCuenca,
                        layers = 'glaciares_r14:2021q1',
                        fmt ='image/png',
                        transparent = True,
                        name = "Glaciares",
                        control = True,
                        attr = "Mapa de Chile"
                        )
    w.add_to(m)


    codComuna = "CQL_FILTER=COMUNA=" + comuna
    w1 = folium.WmsTileLayer(url = 'https://ide.dataintelligence-group.com/geoserver/glaciares/wms?' + codComuna,
                        layers = 'glaciares:R14_BaseZonGlaciares_2017_2021q1',
                        fmt ='image/png',
                        transparent = True,
                        name = "Glaciares 2",
                        control = True,
                        attr = "Mapa de Chile"
                        )

    
    w1.add_to(m)

    filtro = "CQL_FILTER=REGION=" + codigo
    url = "https://ide.dataintelligence-group.com/geoserver/chile/wms?"

    w2 = folium.WmsTileLayer(url = url + filtro,
                        layers = 'chile:Regiones',
                        fmt ='image/png',
                        transparent = True,
                        name = "Regiones",
                        control = True,
                        attr = "Mapa de Chile"
                        )
    w2.add_to(m)


    folium.TileLayer('openstreetmap').add_to(m)
    folium.TileLayer('cartodbpositron').add_to(m)
    folium.TileLayer('cartodbdark_matter').add_to(m)
    folium.LayerControl().add_to(m)

    return m._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
