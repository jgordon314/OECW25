from flask import Flask, request, redirect, url_for, render_template
import disasters_backend
import new_case_backend

# Initialize Flask
app = Flask(__name__)

# landing page redirects to home
@app.route('/')
def landing_page():
    return home()

@app.route('/home')
def home():
    return render_template('home.html')

# TODO: can maybe preprocess by finding every correlation of movies in advance

#### FRIDGE TO MEAL ####
@app.route('/disasters')
def disasters():
    return render_template('disasters.html')

@app.route('/disasters/result', methods=['POST', 'GET'])
def disasters_result():
    if request.method == 'POST':
        form_data = request.form
        return render_template('disasters_result.html', result = disasters_backend.find_meals(form_data))
    else:
        return disasters()    


#### MOVIE TO RECOMMENDATION ####
@app.route('/new_case')
def new_case():
    return render_template('new_case.html')

#### FRIDGE TO MEAL ####
@app.route('/get_data')
def get_data():
    return render_template('get_data.html')

@app.route('/get_data/result', methods=['POST', 'GET'])
def get_data_result():
    if request.method == 'POST':
        form_data = request.form
        return render_template('get_data_result.html', result = disasters_backend.find_meals(form_data))
    else:
        return get_data()    
    
# #### DEBUG ####
# @app.route('/movie_data')
# def show_data():
#     return ratings_data.to_json()

# @app.route('/movie_data/preview')
# def data_preview():
#     return ratings_data.head().to_html()

if __name__ == '__main__':
    app.run(debug=False)