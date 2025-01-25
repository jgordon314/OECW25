# OECW25
Competitor names: Jack Gordon and Rayed Hamayun

Team name: Panic! At The Disco 

Project name: Disaster Tracker O3

# Compilation Instructions
Ensure you have ```python3``` installed. 

Ensure you have all required packages installed (```pip install -r requirements.txt``` in terminal). You may want to do this in a virtual environment.  

Add a Google Maps API key into ```.env```.

Run ```app.py``` as you would a python file (generally, this is done by ```python app.py``` in terminal). 

On your preferred web browser, open the URL printed in terminal (generally, this is ```http://127.0.0.1:5000```).
<br>
<br>
You can now navigate the website. 

# How to use
View nearby declarations of disasters in the Home tab.

Create new kinds of disasters in the Disasters tab.

Report on a disaster using the New Case tab.

Download all the data in a csv format in the Get Data tab.

# Key Aspects of Code
This is a Flask website that relies on website pages either reading CSV files or writing CSV files. 

app.py contains the Flask functions. These pass information into HTML files. 

