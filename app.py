from flask import Flask, request, redirect, url_for, render_template, send_file
import csv
import os
from dotenv import load_dotenv

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
                     'Hurricane/Typhoon'
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
    with open(CASES_CSV_PATH, mode = 'r', encoding="utf8") as file:
        reader = csv.reader(file)
        counter = 0
        for row in reader: 
            try:
                if (counter > 100):
                    break
                else: 
                    single_case = []
                    single_case.append(row[0])
                    single_case.append(f"{row[2]},{row[3]}")
                    case_info.append(single_case)
                    counter += 1
            except: 
                pass
    print(case_info)
    return render_template('home.html', SOURCE="https://www.google.com/maps/embed/v1/place?key="+googleMapsKey+"&q=Eiffel+Tower,Paris+France", case_info=case_info)

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
    return render_template('new_case.html', disaster_names=disaster_names)

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