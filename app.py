from flask import Flask, request, redirect, url_for, render_template, send_file
import csv
import os
from dotenv import load_dotenv

load_dotenv()
googleMapsKey = os.environ.get('GOOGLE_MAPS_KEY')
print(googleMapsKey)

DISASTERS_CSV_PATH = 'disasters.csv'
CASES_CSV_PATH     = 'cases.csv'


# Initialize Flask
app = Flask(__name__)

# landing page redirects to home
@app.route('/')
def landing_page():
    return home()

@app.route('/home')
def home():
    print(googleMapsKey)
    return render_template('home.html', SOURCE = "https://www.google.com/maps/embed/v1/place?key="+googleMapsKey+"&q=Eiffel+Tower,Paris+France")

#### DISASTERS ####
@app.route('/disasters')
def disasters():
    with open(DISASTERS_CSV_PATH, mode = 'r', encoding="utf8") as file:
        reader = csv.reader(file)
        rows = []
        for row in reader: 
            rows.append(row)
        return render_template("disasters.html", csv=rows)

@app.route('/disasters/result', methods=['POST', 'GET'])
def disasters_result():
    if request.method == 'POST':
        form_data = dict(request.form)
        row = []
        for value in form_data.values():
            row.append(value)
        with open(DISASTERS_CSV_PATH,'a') as file:
            writer = csv.writer(file)
            writer.writerow(row)
    return disasters()    


#### NEW CASE ####
@app.route('/new_case')
def new_case():
    print("Showing new case")
    return render_template('new_case.html')

@app.route('/new_case/result', methods=['POST', 'GET'])
def new_case_result():
    if request.method == 'POST':
        form_data = dict(request.form)
        row = []
        for value in form_data.values():
            row.append(value)
        with open(CASES_CSV_PATH,'a') as file:
            writer = csv.writer(file)
            writer.writerow(row)
    return new_case()

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
    
@app.route('/get_data/result', methods=['POST', 'GET'])
def get_data_result():
    if request.method == 'POST':
        form_data = request.form
        return render_template('get_data_result.html', result = disasters_backend.find_meals(form_data))
    else:
        return get_data()    

if __name__ == '__main__':
    app.run(debug=True)