from os import stat
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
import json
import requests
import geopandas as gpd
from shapely.geometry import shape
import branca.colormap as cm
from branca.element import Template, MacroElement

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
    mediambiente = f"{url}/Medioambiente.json"

    m = folium.Map(
        location=[-33.48621795345005, -70.66557950912359],
        zoom_start=5,
        control_scale=True
        # tiles = "openstreetmap"
    )

    def getcolor(feature):
        if feature['properties']['averdexhab'] >= 1.0 and feature['properties']['averdexhab'] <= 5.0:
            return '#a7f77d'
        if feature['properties']['averdexhab'] >= 6.0 and feature['properties']['averdexhab'] <= 10.0:
            return '#71c445'
        if feature['properties']['averdexhab'] >= 11.0 and feature['properties']['averdexhab'] <= 100.0:
            return '#52d50c'
        else:
            return 'transparent'

    folium.GeoJson(mediambiente, 
                    name="Medioambiente",
                    style_function = lambda feature: {
                    'fillColor': getcolor(feature),
                    'weight': 0,
                    'fillOpacity': 0.8,},
                    tooltip = folium.GeoJsonTooltip(fields=["REGION", "COMUNA", "areaverde", "averdexhab"],
                    aliases = ['Región', 'Comuna', 'Área verde', 'Área verde por habitante'],
                    )
    ).add_to(m)

    template = """
    {% macro html(this, kwargs) %}

    <!doctype html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Dataintelligence</title>
    <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

    <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
    
    <script>
    $( function() {
        $( "#maplegend" ).draggable({
                        start: function (event, ui) {
                            $(this).css({
                                right: "auto",
                                top: "auto",
                                bottom: "auto"
                            });
                        }
                    });
    });

    </script>
    </head>
    <body>

    
    <div id='maplegend' class='maplegend' 
        style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
        border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 20px;'>
        
    <div class='legend-title'>Área verde por habitante</div>
    <div class='legend-scale'>
    <ul class='legend-labels'>
        <li><span style='background:#a7f77d;opacity:0.7;'></span>1 - 5</li>
        <li><span style='background:#71c445;opacity:0.7;'></span>6 - 10</li>
        <li><span style='background:#52d50c;opacity:0.7;'></span>11 - 100</li>

    </ul>
    </div>
    </div>
    
    </body>
    </html>

    <style type='text/css'>
    .maplegend .legend-title {
        text-align: left;
        margin-bottom: 5px;
        font-weight: bold;
        font-size: 90%;
        }
    .maplegend .legend-scale ul {
        margin: 0;
        margin-bottom: 5px;
        padding: 0;
        float: left;
        list-style: none;
        }
    .maplegend .legend-scale ul li {
        font-size: 80%;
        list-style: none;
        margin-left: 0;
        line-height: 18px;
        margin-bottom: 2px;
        }
    .maplegend ul.legend-labels li span {
        display: block;
        float: left;
        height: 16px;
        width: 30px;
        margin-right: 5px;
        margin-left: 0;
        border: 1px solid #999;
        }
    .maplegend .legend-source {
        font-size: 80%;
        color: #777;
        clear: both;
        }
    .maplegend a {
        color: #777;
        }
    </style>
    {% endmacro %}"""

    macro = MacroElement()
    macro._template = Template(template)

    m.get_root().add_child(macro)

    return m._repr_html_()

if __name__ == '__main__':
    app.run()
