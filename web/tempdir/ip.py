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

#Put the information in a dataframe
json_data = pd.DataFrame([json_data])

#Drop the unnecessary columns
json_data.drop(columns=['in_eu', 'languages','country_code','country_code_iso3','region',
                        'country_capital','country_tld','continent_code','country_population',
                        'country_calling_code','region_code'],inplace=True)

#Rename the columns for a better readable format
json_data.rename(columns={'ip':'IP','network':'Network','version':'Version','city':'City',
    'region':'Region','country_name':'Country','latitude':'Latitude','longitude':'Longitude',
    'timezone':'Timezone','utc_offset':'UTC Offset','currency':'Currency','currency_name':'Currency Name',
    'country_area':'Country Area','asn':'ASN','org':'ISP','country':'Country Code','postal':'Postal'}, inplace=True)

#Reshape the dataframe to make it a long table
json_data = json_data.melt()

#Rename the new columns
json_data.rename(columns={'variable': 'Information', 'value': 'Value'}, inplace=True)

@app.route('/')
def man():
    return render_template('index.html', tables=[json_data.to_html(index=False)], titles=['Information','Value'])

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
