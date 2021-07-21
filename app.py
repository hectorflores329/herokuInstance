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
import random
import requests
import geopandas

app = Flask(__name__)

@app.route('/')
# def mapa(codigo = '15'):
def mapa():

    url = (
        "https://raw.githubusercontent.com/hectorflores329/herokugee/main"
    )
    antarctic_ice_edge = f"{url}/_ICVU_2019.json"

    codigo = request.args.get("codigo")
    codigo = str(codigo)

    comuna = request.args.get("comuna")
    comuna = str(comuna)

    # atlas = folium.raster_layers.WmsTileLayer(url = 'https://ide.dataintelligence-group.com/geoserver/chile/wms?', layers='chile:Regiones', name='test', fmt='image/png', attr='test', transparent=True, version='1.3.0')

    m = folium.Map(
        location=[-33.48621795345005, -70.66557950912359],
        zoom_start=5,
        min_zoom = 8,
        max_zoom = 30,
        control_scale=True
        # tiles = "openstreetmap"
        )

    w = folium.WmsTileLayer(url = 'https://ide.dataintelligence-group.com/geoserver/glaciares_r14/wms?',
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

    folium.GeoJson(antarctic_ice_edge, 
                    name="Comunas GEO",
                    tooltip=folium.GeoJsonTooltip(fields=["COMUNA", "ICVU"])
                    ).add_to(m)
    
    folium.TileLayer('openstreetmap').add_to(m)
    folium.TileLayer('cartodbpositron').add_to(m)
    folium.TileLayer('cartodbdark_matter').add_to(m)
    folium.LayerControl().add_to(m)

    return m._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

@app.route('/tabla')
def tabla():

    url = (
        "https://raw.githubusercontent.com/hectorflores329/herokugee/main"
    )
    state_geo = f"{url}/_ICVU_2019.json"
    # state_unemployment = f"{url}/US_Unemployment_Oct2012.csv"
    state_data = pd.read_csv(state_geo)

    m = folium.Map(location=[-33.48621795345005, -70.6655795091235], zoom_start=3)

    folium.Choropleth(
        geo_data=state_geo,
        name="choropleth",
        data=state_data,
        columns=["CUT_COM", "COMUNA"],
        # key_on="feature.id",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Unemployment Rate (%)",
    ).add_to(m)

    folium.LayerControl().add_to(m)

    #return df.to_html(header="true", table_id="table")
    return m._repr_html_()

if __name__ == '__main__':
    app.run()
