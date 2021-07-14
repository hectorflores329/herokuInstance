from flask import Flask
import pandas as pd
import folium
from folium.plugins import HeatMapWithTime

df = pd.DataFrame({'Lat': [40.784217, 40.762797, 40.721856, 40.755798, 40.711786],
                   'Long': [-73.846007, -73.865112, -73.852954, -73.940719, -73.859124],
                   'Confirmed': [20, 30, 40, 50, 60]})


app = Flask(__name__)

@app.route('/')
def hello_world():

    new_map = folium.Map(location=[40.712776, -74.005974], tiles= "Puntos",min_zoom=2, zoom_start=2, max_zoom=3)

    df['Lat'] = df['Lat'].astype(float)
    df['Long'] = df['Long'].astype(float)

    Confirmed_df = df[['Lat', 'Long','Confirmed']]

    hm = HeatMapWithTime(Confirmed_df,auto_play=True,max_opacity=0.8)
    hm.add_to(new_map)    

    return new_map._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

@app.route('/tabla')
def tabla():
    return df.to_html(header="true", table_id="table")

if __name__ == '__main__':
    app.run()
