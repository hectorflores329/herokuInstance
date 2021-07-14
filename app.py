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

    m = folium.Map([48.0, 5.0], tiles="stamentoner", zoom_start=6)

    hm = plugins.HeatMapWithTime(data, index=time_index, auto_play=True, max_opacity=0.3)

    hm.add_to(m)
      

    return m._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
