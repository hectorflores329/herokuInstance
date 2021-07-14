import folium
import folium.plugins as plugins
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello_world():

    np.random.seed(3141592)
    initial_data = np.random.normal(size=(100, 2)) * np.array([[1, 1]]) + np.array(
        [[48, 5]]
    )

    move_data = np.random.normal(size=(100, 2)) * 0.01

    data = [(initial_data + move_data * i).tolist() for i in range(100)]

    weight = 1  # default value
    for time_entry in data:
        for row in time_entry:
            row.append(weight)

    m = folium.Map([48.0, 5.0], tiles="stamentoner", zoom_start=6)

    hm = plugins.HeatMapWithTime(data)

    hm.add_to(m)
      

    return m._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
