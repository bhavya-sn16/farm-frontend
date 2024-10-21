from flask import Flask, render_template,request, url_for,flash,redirect,jsonify,send_from_directory
import requests



app  = Flask(__name__)


# @app.route('/')
# def table():
#    print("nnnnnnn")
#    return render_template('table.html')     

@app.route('/')
def display_sensor_data():
    
    fastapi_url = "http://127.0.0.1:8000/getdata"  
    response = requests.get(fastapi_url, params={})

    
    if response.status_code == 200:
        data = response.json().get('data')
    else:
        data = []

 
    return render_template('table.html', data=data)   
    
# @app.route('/')
# def display_sensor_data():
#     return render_template('table.html')


if __name__ == '__main__':
    app.run(debug=True)     