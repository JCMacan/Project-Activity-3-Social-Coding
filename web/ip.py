import requests
from flask import Flask, render_template, request
import flask
app = Flask(__name__)
from flask_cors import CORS
CORS(app)
import pandas as pd

ip = requests.get('https://ip4.seeip.org/').text

main_api = "https://ipapi.co/"

url = main_api + ip + "/json"

json_data = requests.get(url).json()
json_data = pd.DataFrame([json_data])
json_data.drop(columns=['in_eu', 'languages','country_code','country_code_iso3'],inplace=True)
json_data = json_data.melt()
json_data.rename(columns={'variable': 'Information', 'value': 'Value'}, inplace=True)
json_data.info()
def man():
    return render_template('index.html', tables=[json_data.to_html(index=False)], titles=['Information','Value'])

if __name__ == "__main__":
    app.run(debug=True)
