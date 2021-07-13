from flask import Flask
import folium
from django.shortcuts import render

app = Flask(__name__)


@app.route("/")
def show_map(request):
    m = folium.Map(location=[55.17, 51.00], tiles='OpenStreetMap', name="Light Map",
                   zoom_start=6, attr="My Data attribution")
    folium.features.GeoJson(data= "all_id.geojson"
                            , name="States", popup=folium.features.GeoJsonPopup(fields=["rname", "id"],
                                                                                aliases=["region_name",
                                                                                        "region_id"])).add_to(m)
    m = m._repr_html_()
    context = {'my_map': m}

    return render(request, 'map/map_render.html', context) 


if __name__ == "__main__":
    app.run()
