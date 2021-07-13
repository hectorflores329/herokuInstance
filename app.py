from flask import Flask
import pandas as pd
import folium
from folium.plugins import HeatMapWithTime

df = pd.DataFrame({'col1': ['abc', 'def', 'tre'],
                   'col2': ['foo', 'bar', 'stuff']})

app = Flask(__name__)

@app.route('/')
def hello_world():

    
    map_Oslo = folium.Map(location=[-33.48621795345005, -70.66557950912359], zoom_start=5)
    HeatMapWithTime(df, 
                            radius=10,
                    gradient={0.1: 'blue', 0.2: 'blue', 0.4: 'lime', 0.6: 'orange', 0.8: 'red', 0.99: 'purple'},
                    min_opacity=0.5, max_opacity=0.8, use_local_extrema=False).add_to(map_Oslo)
    

    return map_Oslo._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
