from flask import Flask
import folium

app = Flask(__name__)


@app.route("/")
def base():
    base_map = folium.Map(location=[52.2297, 21.0122], control_scale=True, zoom_start=10)

    points1 = [(52.228771, 21.003146),
            (52.238025, 21.050971),
            (52.255008, 21.036172),
            (52.252831, 21.051385),
            (52.219995, 20.965021)
            ]

    train_group = folium.FeatureGroup(name="Trains").add_to(base_map)

    for tuple_ in points1:

        icon=folium.Icon(color='white', icon='train', icon_color="red", prefix='fa')
        train_group.add_child(folium.Marker(tuple_, icon=icon))

    points2 = [(52.239062, 21.131601),
            (52.204905, 21.168202),
            (52.181296, 20.987486),
            (52.206272, 20.914988),
            (52.254395, 21.224107)
            ]

    cars_group = folium.FeatureGroup(name="Cars").add_to(base_map)

    for tuple_ in points2:
        icon=folium.Icon(color='white', icon='car', icon_color="blue", prefix='fa')
        cars_group.add_child(folium.Marker(tuple_, icon=icon))

    line_points = [(52.204905, 21.168202),
                (52.255008, 21.036172), 
                (52.219995, 20.965021), 
                (52.239062, 21.131601), 
                (52.254395, 21.224107)
                ]
    lines_group = folium.FeatureGroup(name="Lines").add_to(base_map)
    lines_group.add_child(folium.PolyLine(locations=line_points, weight=3,color = 'yellow'))

    folium.LayerControl().add_to(base_map)

    base_map.save("example_map.html")


if __name__ == "__main__":
    app.run()
