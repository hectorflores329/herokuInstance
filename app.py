from flask import Flask
import pandas as pd
import folium
from folium.plugins import HeatMapWithTime

df = pd.DataFrame({'col1': ['abc', 'def', 'tre'],
                   'col2': ['foo', 'bar', 'stuff']})

map = folium.Map(location=[40.712776, -74.005974],zoom_start=10)
lat_long_list2 = [[[40.784217, -73.846007],[40.762797, -73.86511],[40.721856, -73.852954]],[40.647186, -73.980259]]

_map = HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

app = Flask(__name__)

@app.route('/')
def hello_world():
    # return df.to_html(header="true", table_id="table")
    return _map._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
