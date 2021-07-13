from flask import Flask
import pandas as pd
import folium
from folium.plugins import HeatMapWithTime

df = pd.DataFrame({'col1': ['10',20, 30],
                   'col2': [120, 150, 200]})
time = ['2018-07-04 08:11:54.170000','2018-07-04 08:15:01.910000', '2018-06-04 08:23:09.700000']

lat_long_list2 = [[[40.784217, -73.846007],
  [40.762797, -73.865112],
  [40.721856, -73.852954],
  [40.755798, -73.940719],
  [40.711786, -73.859124],
  [40.647186, -73.980259],
  [40.822739, -73.884387],
  [40.746646000000005, -73.983798],
  [40.6196, -73.917266],
  [40.741264, -73.90277900000001],
  [40.731829, -73.769674],
  [40.779291, -73.804456],
  [40.674646, -73.843312],
  [40.7435, -73.92258199999999],
  [40.640856, -73.955972],
  [40.880219, -73.91733599999999],
  [40.771006, -73.966011],
  [40.758564, -73.977183],
  [40.8968, -73.90781],
  [40.78982, -73.952285],
  [40.752732, -73.97940899999999],
  [40.790273, -73.951957],
  [40.748624, -73.984413],
  [40.74686, -73.98364000000001],
  [40.765415000000004, -73.970084],
  [40.787639, -73.955937],
  [40.751956, -73.979987],
  [40.791641999999996, -73.94465100000001],
  [40.752306, -73.924666],
  [40.679293, -73.863691],
  [40.702846, -73.801998],
  [40.741803000000004, -73.90528499999999],
  [40.593964, -73.789386],
  [40.573484, -73.854108],
  [40.769804, -73.886821],
  [40.765351, -73.918021],
  [40.76509, -73.93185],
  [40.757809, -73.954877],
  [40.709433000000004, -73.869708],
  [40.733292999999996, -73.872233],
  [40.75257, -73.943826],
  [40.598457, -73.909942],
  [40.709517, -73.835102],
  [40.696189000000004, -73.804457],
  [40.570679, -73.872378],
  [40.675452, -73.871773],
  [40.602438, -73.753315],
  [40.672349, -73.843325],
  [40.704924, -73.809093],
  [40.735306, -73.875887],
  [40.770423, -73.87606099999999],
  [40.746727, -73.890458],
  [40.70203, -73.804969],
  [40.674537, -73.802509],
  [40.67796, -73.830396],
  [40.683562, -73.845557],
  [40.711727, -73.729798],
  [40.657474, -73.74611],
  [40.72421, -73.842986],
  [40.788962, -73.822684],
  [40.861216, -73.822711],
  [40.76023, -73.879579],
  [40.742629, -73.895655],
  [40.726352, -73.89541],
  [40.770196999999996, -73.87556500000001],
  [40.847476, -73.82722700000001],
  [40.676087, -73.867499],
  [40.707575, -73.79324799999999],
  [40.667055, -73.789378],
  [40.714057000000004, -73.830081],
  [40.705267, -73.79547099999999],
  [40.678336, -73.799626],
  [40.740908000000005, -73.933071],
  [40.733589, -73.864253],
  [40.746678, -73.890746],
  [40.706521, -73.86893],
  [40.758003, -73.92863],
  [40.703524, -73.799925],
  [40.761076, -73.963443],
  [40.605754, -73.914816],
  [40.640772, -73.965477],
  [40.684425, -73.978462],
  [40.706936999999996, -73.854407],
  [40.684943, -73.980975],
  [40.669989, -73.809441],
  [40.66681, -73.810425],
  [40.6914, -73.826697],
  [40.646984, -73.779262],
  [40.669878000000004, -73.809474],
  [40.605132, -73.754703],
  [40.707515, -73.803377],
  [40.689529, -73.786101],
  [40.60279, -73.750098],
  [40.705822, -73.801677],
  [40.657455999999996, -73.74521899999999],
  [40.78492, -73.856858],
  [40.754763, -73.89375799999999],
  [40.643924, -73.958475],
  [40.752259, -73.82083399999999],
  [40.699201, -73.807025],
  [40.733307, -73.872465],
  [40.701786, -73.807671],
  [40.580326, -73.837396],
  [40.652303, -73.838071],
  [40.580286, -73.835631],
  [40.693582, -73.85239399999999],
  [40.760226, -73.830455],
  [40.701785, -73.807885],
  [40.755258000000005, -73.865236],
  [40.773001, -73.84559899999999],
  [40.737572, -73.804591],
  [40.792021999999996, -73.850436],
  [40.731525, -73.87162],
  [40.762989000000005, -73.83521800000001],
  [40.756006, -73.880873],
  [40.720046, -73.88998000000001],
  [40.732535, -73.857088],
  [40.734212, -73.850246],
  [40.776209, -73.901999],
  [40.751598, -73.886768],
  [40.784287, -73.886821],
  [40.765575, -73.88734699999999],
  [40.738977, -73.917635],
  [40.713526, -73.87164399999999],
  [40.860383, -73.890901],
  [40.881839, -73.896362],
  [40.874352, -73.909348],
  [40.834763, -73.917704],
  [40.856922999999995, -73.880989],
  [40.835402, -73.832619],
  [40.878642, -73.871581],
  [40.841724, -73.883661],
  [40.798371, -73.920947],
  [40.823941, -73.893327],
  [40.793618, -73.921585],
  [40.607076, -74.015941],
  [40.645845, -73.99493000000001],
  [40.624997, -74.017663],
  [40.588827, -73.990376],
  [40.667589, -73.994254],
  [40.635275, -74.037522],
  [40.729755, -73.993114],
  [40.687799, -73.98706899999999],
  [40.574159, -74.17005400000001],
  [40.637006, -73.995409],
  [40.765909, -73.976791],
  [40.708504, -74.012473],
  [40.608408000000004, -74.039203],
  [40.562406, -74.19354799999999],
  [40.536042, -74.157173],
  [40.765042, -73.97666600000001],
  [40.621328000000005, -74.02313000000001],
  [40.633685, -74.136302],
  [40.689208, -73.99090100000001],
  [40.761581, -73.974979],
  [40.735617, -73.989712],
  [40.537064, -74.15835799999999],
  [40.629419, -74.14089200000001],
  [40.608198, -74.138912],
  [40.625448999999996, -74.143636],
  [40.610787, -74.119893],
  [40.624913, -74.146771],
  [40.761194, -73.969767],
  [40.555313, -74.12955],
  [40.716221000000004, -74.004584],
  [40.727191, -73.995285],
  [40.547259000000004, -74.166221],
  [40.541894, -74.16289300000001],
  [40.546496999999995, -74.181678],
  [40.539505, -74.160655],
  [40.830588, -73.861659],
  [40.614575, -74.02805500000001],
  [40.834926, -73.948941],
  [40.85183, -73.89842],
  [40.810024, -73.87623599999999],
  [40.810159000000006, -73.875341],
  [40.835634000000006, -73.895388],
  [40.829825, -73.89829399999999],
  [40.824039, -73.858746],
  [40.834439, -73.91719499999999],
  [40.820570000000004, -73.851549],
  [40.84813, -73.937017],
  [40.81151, -73.85470500000001],
  [40.730413, -73.954299],
  [40.620090000000005, -74.02741999999999],
  [40.610799, -73.991692],
  [40.650818, -74.004372],
  [40.649976, -73.9808],
  [40.651441999999996, -73.963243],
  [40.625625, -74.040184],
  [40.646915, -74.01181],
  [40.658417, -73.98571],
  [40.763171, -73.985461],
  [40.70456, -74.01435699999999],
  [40.732921000000005, -74.007287],
  [40.70653, -74.013865],
  [40.74228, -73.989011],
  [40.72477, -73.974923],
  [40.633534999999995, -73.967137],
  [40.821641, -73.93700799999999],
  [40.77265, -73.98209200000001],
  [40.640657, -74.014946],
  [40.786984999999994, -73.977521],
  [40.819229, -73.947024],
  [40.735465999999995, -73.994006],
  [40.768724, -73.981429],
  [40.758633, -73.99248399999999],
  [40.800515999999995, -73.965654],
  [40.784196, -73.946976],
  [40.804636, -73.955885],
  [40.804521, -73.955611],
  [40.768074, -73.97024300000001],
  [40.802747, -73.958497],
  [40.813169, -73.93732800000001],
  [40.739633000000005, -73.995182],
  [40.781597, -73.958274],
  [40.759485999999995, -73.995143],
  [40.757646, -73.960465],
  [40.774267, -73.988515],
  [40.658467, -73.98565699999999],
  [40.760319, -73.99712199999999],
  [40.75347, -73.967152],
  [40.715423, -74.014673],
  [40.745694, -73.998194],
  [40.713295, -73.977739],
  [40.794998, -73.972613],
  [40.814856, -73.955189],
  [40.797465, -73.930853],
  [40.848304999999996, -73.93743],
  [40.652491999999995, -74.005943],
  [40.686603000000005, -73.947237],
  [40.707770000000004, -73.946463],
  [40.699451, -73.912699],
  [40.685694, -73.916013],
  [40.687355, -73.913619],
  [40.703381, -73.903541],
  [40.673704, -73.944572],
  [40.694872, -73.990697],
  [40.677183, -73.89739300000001],
  [40.692240000000005, -73.989305],
  [40.706384, -73.917117],
  [40.736571000000005, -73.877494],
  [40.735209000000005, -73.93727700000001],
  [40.698547, -73.941086],
  [40.759972, -73.823642],
  [40.694431, -73.914695],
  [40.590625, -74.192541],
  [40.584809, -74.160358],
  [40.654608, -73.921838],
  [40.757355, -73.829488]]]

app = Flask(__name__)

@app.route('/')
def hello_world():

    
    _map = folium.Map(
        location=[40.712776, -74.005974],
        zoom_start=5,
        width = 850,
        height = 650,
        min_zoom = 8,
        max_zoom = 14
        )

    '''HeatMapWithTime(lat_long_list2, radius=10, gradient={0.1: 'blue', 0.2: 'blue', 0.4: 'lime', 0.6: 'orange', 0.8: 'red', 0.99: 'purple'},
                    min_opacity=0.5, max_opacity=0.8, use_local_extrema=False, auto_play=True,position='bottomright').add_to(map_Oslo)'''

    HeatMapWithTime(lat_long_list2, index=time, radius=5, auto_play=True, position='bottomleft').add_to(_map)
    

    return _map._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

@app.route('/tabla')
def tabla():
    return df.to_html(header="true", table_id="table")

if __name__ == '__main__':
    app.run()
