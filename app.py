from flask import Flask
import folium
import folium.plugins as plugins
import numpy as np
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def hello_world():

    np.random.seed(3141592)
    initial_data = np.random.normal(size=(100, 2)) * np.array([[1, 1]]) + np.array(
        [[48, 5]]
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

    m = folium.Map(
        location=[48.0, 5.0],
        zoom_start=2,
        width = 850,
        height = 650,
        min_zoom = 8,
        max_zoom = 30
        )

    hm = plugins.HeatMapWithTime(data, index=time_index, auto_play=True, max_opacity=0.3, position='bottomright')

    hm.add_to(m)
    
    folium.Marker(
        location=[48.0, 5.0],
        popup="Este es un ícono o marca",
        icon=folium.Icon(icon="cloud"),
    ).add_to(m)

    folium.CircleMarker(
        location=[48.0, 5.0],
        radius=50,
        popup="Laurelhurst Park",
        color="#3186cc",
        fill=True,
        fill_color="#3186cc",
    ).add_to(m)

    return m._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
