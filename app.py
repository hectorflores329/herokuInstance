from flask import Flask
import folium
import pandas as pd

app = Flask(__name__)

# Importing Data
df = pd.read_csv('mta_1712.csv', error_bad_lines=False)

# Getting data for 1 December 2017
df=df[df['RecordedAtTime'].str.split(' ').apply(lambda x:x[0]=='2017-12-01')]

df=df[['RecordedAtTime','VehicleRef','VehicleLocation.Latitude','VehicleLocation.Longitude']]
df.duplicated().value_counts()

df=df.drop_duplicates()
df.isnull().sum()

df2=pd.DataFrame(df.groupby(['hour','VehicleRef'])['RecordedAtTime'].max())
df2.reset_index(inplace=True)

df3=pd.merge(df2,df,left_on=['hour','VehicleRef','RecordedAtTime'],right_on=['hour','VehicleRef','RecordedAtTime'])

# Converting column to datetime
df['RecordedAtTime']=pd.to_datetime(df['RecordedAtTime'],format='%Y-%m-%d %H:%M:%S')
# Creating hour column
df['hour']=df['RecordedAtTime'].apply(lambda x: x.hour+1)

lat_long_list = []
for i in range(1,25):
    temp=[]
    for index, instance in df3[df3['hour'] == i].iterrows():
        temp.append([instance['VehicleLocation.Latitude'],instance['VehicleLocation.Longitude']])
    lat_long_list.append(temp)




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
