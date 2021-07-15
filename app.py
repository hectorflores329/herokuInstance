from flask import Flask
import folium
import folium.plugins as plugins
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from folium.plugins import FloatImage
from folium.plugins import Draw
from folium.plugins import MiniMap

app = Flask(__name__)

@app.route('/')
def mapa():

    _data = pd.DataFrame({
        'lon':[-58, 2, 145, 30.32, -4.03, -73.57, 36.82, -38.5],
        'lat':[-34, 49, -38, 59.93, 5.33, 45.52, -1.29, -12.97],
        'name':['Buenos Aires', 'Paris', 'melbourne', 'St Petersbourg', 'Abidjan', 'Montreal', 'Nairobi', 'Salvador'],
        'value':[10, 12, 40, 70, 23, 43, 100, 43]
    })

    np.random.seed(3141592)
    initial_data = np.random.normal(size=(100, 2)) * np.array([[1, 1]]) + np.array(
        [[-33.48621795345005, -70.66557950912359]]
    )

    move_data = np.random.normal(size=(100, 2)) * 0.01

    data = [(initial_data + move_data * i).tolist() for i in range(100)]

    time_index = [
        (datetime.now() + k * timedelta(1)).strftime("%Y-%m-%d") for k in range(len(data))
    ]

    weight = 1  # default value
    for time_entry in data:
        for row in time_entry:
            row.append(weight)

    # atlas = folium.raster_layers.WmsTileLayer(url = 'https://ide.dataintelligence-group.com/geoserver/chile/wms?', layers='chile:Regiones', name='test', fmt='image/png', attr='test', transparent=True, version='1.3.0')

    m = folium.Map(
        location=[-33.48621795345005, -70.66557950912359],
        zoom_start=5,
        min_zoom = 8,
        max_zoom = 30,
        control_scale=True
        # tiles = "openstreetmap"
        )

    w = folium.WmsTileLayer(url = 'https://ide.dataintelligence-group.com/geoserver/chile/wms',
                        layers = 'chile:Regiones',
                        fmt ='image/png',
                        transparent = True,
                        name = "Regiones",
                        control = True,
                        attr = "Mapa de Chile"
                        )

    w.add_to(m)

    hm = plugins.HeatMapWithTime(data, index=time_index, name="Puntos", auto_play=True, max_opacity=0.3, position='bottomright')

    hm.add_to(m)
    
    '''folium.Marker(
        location=[-33.48621795345005, -70.66557950912359],
        popup="Esto es una marca estática.",
        icon=folium.Icon(icon="cloud"),
    ).add_to(m)

    folium.CircleMarker(
        location=[-33.047971387856414, -71.61855844930044],
        radius=50,
        popup="Circunferencia estática ubicada en Valparaíso.",
        color="#3186cc",
        fill=True,
        fill_color="#3186cc",
    ).add_to(m)'''

    folium.TileLayer('openstreetmap').add_to(m)
    folium.TileLayer('cartodbpositron').add_to(m)
    folium.TileLayer('cartodbdark_matter').add_to(m)
    folium.LayerControl().add_to(m)

    url = (
        "https://github.com/hectorflores329/herokuinstance/raw/main/dataintelligence.png"
    )

    FloatImage(url, bottom=1, left=8).add_to(m)

    draw = Draw(export=True)

    draw.add_to(m)

    minimap = MiniMap(toggle_display=True)
    minimap.add_to(m)

    for i in range(0,len(_data)):
        folium.Marker(
            location=[_data.iloc[i]['lat'], _data.iloc[i]['lon']],
            popup=_data.iloc[i]['name']
        ).add_to(m)

    return m._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
