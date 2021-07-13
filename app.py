from flask import Flask
import folium

app = Flask(__name__)


@app.route("/")
def base():
    # this is base map
    map = folium.Map(
        location=[-33.48621795345005, -70.66557950912359]
    )
    return map._repr_html_()


if __name__ == "__main__":
    app.run()