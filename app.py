from flask import Flask
import folium
import pandas as pd

app = Flask(__name__)


@app.route("/")
def base():

    # this is base map
    map = folium.Map(
        location=[-33.48621795345005, -70.66557950912359],
        width = 750,
        height = 550,
        zoom_start = 5,
        min_zoom = 8,
        max_zoom = 14
    )

    folium.TileLayer('Stamen Terrain').add_to(map)
    folium.TileLayer('Stamen Toner').add_to(map)
    folium.TileLayer('Stamen Water Color').add_to(map)
    folium.TileLayer('cartodbpositron').add_to(map)
    folium.TileLayer('cartodbdark_matter').add_to(map)
    folium.LayerControl().add_to(map)

    return map._repr_html_()


if __name__ == "__main__":
    app.run()
