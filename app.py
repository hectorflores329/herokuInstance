from flask import Flask
import pandas as pd
import folium
from folium.plugins import HeatMapWithTime

df = pd.DataFrame({'col1': [10,20, 30],
                   'col2': [120, 150, 200]})

lat_long_list2 = [[[40.784217, -73.846007],[40.762797, -73.86511],[40.721856, -73.852954]],[40.647186, -73.980259]]

app = Flask(__name__)

@app.route('/')
def hello_world():

    
    map_Oslo = folium.Map(location=[-33.48621795345005, -70.66557950912359], zoom_start=5)
    HeatMapWithTime(lat_long_list2, radius=10).add_to(map_Oslo)
    

    return map_Oslo._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
