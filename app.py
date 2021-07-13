from flask import Flask
import pandas as pd

df = pd.DataFrame({'col1': ['abc', 'def', 'tre'],
                   'col2': ['foo', 'bar', 'stuff']})



app = Flask(__name__)

@app.route('/')
def hello_world():
    return df.to_html(header="true", table_id="table")

if __name__ == '__main__':
    app.run()
