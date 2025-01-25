from flask import Flask, request, redirect, url_for, render_template, send_file
import csv
import os
from dotenv import load_dotenv
import time
import pandas as pd

load_dotenv()
googleMapsKey = os.environ.get('GOOGLE_MAPS_KEY')
print(googleMapsKey)

DISASTERS_CSV_PATH = 'disasters.csv'
CASES_CSV_PATH     = 'cases.csv'

DISASTER_CATEGORIES=['Disease',
                     'Earthquake',
                     'Tsunami',
                     'Wildfire',
                     'Blizzard',
                     'Avalanche',
                     'Flood',
                     'Heat Wave',
                     'Landslide',
                     'Tornado',
                     'Hurricane/Typhoon',
                     'Other'
                    ]

# Initialize Flask
app = Flask(__name__)

# landing page redirects to home
@app.route('/')
def landing_page():
    return home()

@app.route('/home')
def home():
    case_info = []

    # Read the CSV file into a dataframe
    df = pd.read_csv(CASES_CSV_PATH, encoding="utf8")

    # Sort dataframe by greatest (most recent) time to get 100 most recent pins
    df = df.sort_values(by=df.columns[1], ascending=False)
    df = df.head(100)
    
    # Get disaster information from dataframe
    disaster_names = df.iloc[:, 0].astype(str).tolist()
    disaster_latitudes = df.iloc[:, 2].astype(str).tolist()
    disaster_longitudes = df.iloc[:, 3].astype(str).tolist()

    # Combine information; this is to be turned into pins
    case_info = [[disaster_names[i], f"{disaster_latitudes[i]},{disaster_longitudes[i]}"] for i in range(len(disaster_names))]

    return render_template('home.html', API_KEY=googleMapsKey, case_info=case_info)

#### DISASTERS ####
@app.route('/disasters')
def disasters():
    with open(DISASTERS_CSV_PATH, mode = 'r', encoding="utf8") as file:
        reader = csv.reader(file)
        return render_template("disasters.html", csv=reader, disaster_categories = DISASTER_CATEGORIES)

@app.route('/disasters/result', methods=['POST', 'GET'])
def disasters_result():
    if request.method == 'POST':
        form_data = dict(request.form)
        row = []
        for value in form_data.values():
            row.append(value)
        with open(DISASTERS_CSV_PATH,'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)
    return render_template("disasters_result.html")


#### NEW CASE ####
@app.route('/new_case')
def new_case():
    disaster_names = []
    with open(DISASTERS_CSV_PATH, mode = 'r', encoding="utf8") as file:
        reader = csv.reader(file)
        for row in reader: 
            disaster_names.append(row[0])
    return render_template('new_case.html', disaster_names=disaster_names, TIME = time.strftime("%Y-%m-%dT%H:%M"))

@app.route('/new_case/result', methods=['POST', 'GET'])
def new_case_result():
    if request.method == 'POST':
        form_data = dict(request.form)
        row = []
        for value in form_data.values():
            row.append(value)
        with open(CASES_CSV_PATH,'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)
    return render_template('new_case_result.html')

#### GET DATA ####
@app.route('/get_data')
def get_data():
    return render_template('get_data.html')

@app.route("/download/disasters")
def disasters_dl():
    return send_file(DISASTERS_CSV_PATH, as_attachment=True)

@app.route("/download/cases")
def cases_dl():
    return send_file(CASES_CSV_PATH, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)