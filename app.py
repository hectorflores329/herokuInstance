from flask import Flask

import folium
import pandas as pd
import geopandas as gpd
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # Accessing API data using the python "requests" module
    response = requests.get("https://ng-covid-19-api.herokuapp.com/")
    data_json = response.json()

    # Loading the Nigeria geojson file as a pandas Dataframe using "geopandas" python package
    df = gpd.read_file("The_Naija_Poly.geojson")

    folium_map = folium.Map(location = [9.0820, 8.6753],tiles = "Mapbox Control Room", zoom_start = 6, min_zoom = 6, max_zoom = 7,
                    max_lat =16 , max_lon =15 , min_lat = 2 , min_lon =1, max_bounds = True )

    folium.LayerControl().add_to(folium_map) 

    return folium_map._repr_html_()

if __name__ == "__main__":
    app.run()