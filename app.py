from flask import Flask, render_template,request, url_for,flash,redirect,jsonify,send_from_directory
import requests
from datetime import datetime



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

    print(data)
    return render_template('table.html', data=data)   

@app.route('/getdata',methods=['GET'])
def display_sensor_data_withDate():

    selected_date = request.args.get('date')
    # date_part, time_part = selected_date.split('T')
    # formatted_date = date_part.replace('-', '/')
    
    fastapi_url = "http://127.0.0.1:8000/getdata"  
    response = requests.get(fastapi_url, params={"date": selected_date})
    print(selected_date)

    
    if response.status_code == 200:
        data = response.json().get('data')
    else:
        data = []
    print(data)
    return render_template('reload.html', data=data)




# @app.route('/getdata')
# def display_sensor_data():
    
#     fastapi_url = "http://127.0.0.1:8000/getdata"  
#     response = requests.get(fastapi_url, params={})

    
#     if response.status_code == 200:
#         data = response.json().get('data')
#     else:
#         data = []

 
#     return render_template('table.html', data=data)  
    
# @app.route('/')
# def display_sensor_data():
#     return render_template('table.html')

if __name__ == '__main__':
    app.run(debug=True)     