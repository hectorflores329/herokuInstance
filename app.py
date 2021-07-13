from flask import Flask
import pandas as pd

df = pd.DataFrame({'col1': ['abc', 'def', 'tre'],
                   'col2': ['foo', 'bar', 'stuff']})


lat_long_list2 = [[[40.784217, -73.846007],[40.762797, -73.86511],[40.721856, -73.852954]],[40.647186, -73.980259]]

app = Flask(__name__)

@app.route('/')
def hello_world():
    return df.to_html(header="true", table_id="table")

if __name__ == '__main__':
    app.run()
