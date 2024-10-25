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
    print(response)
    if response.status_code == 200:
        data = response.json().get('data')
    else:
        data = []

    return render_template('table.html', data=data)   

@app.route('/getData',methods = ['GET','POST'])
def data_withDate():

    selected_date = request.args.get('date')
    print(selected_date)

    # date_part, time_part = selected_date.split('T')
    # formatted_date = date_part.replace('-', '/')
    
    fastapi_url = "http://127.0.0.1:8000/getdata"  
    response = requests.get(fastapi_url, params={"date":selected_date})
    print(response)
    if response.status_code == 200:
        data = response.json().get('data')
        
    else:
        data = []
    print(data)
    return render_template('partials/reload.html', data=data)

@app.route('/chartData', methods=['GET', 'POST'])
def chart_withDate():
    selected_date = request.args.get('date')
    

    fastapi_url = "http://127.0.0.1:8000/getdata"
    response = requests.get(fastapi_url, params={"date": selected_date})

    if response.status_code == 200:
        data = response.json().get('data')
    else:
        data = []
    print(data)
    print(f"Selected Date: {selected_date}")
    return render_template('partials/chart.html', data=data)

@app.template_filter("strftime")
def format_datetime(value, format="%Y-%m-%d"):
    """Format a datetime object as a string."""
    if isinstance(value, datetime):
        return value.strftime(format)
    return value  # Return unformatted if value is not a datetime
   
@app.template_filter("str_to_date")
def str_to_date(date_string, format_string="%Y/%m/%d %H:%M:%S"):
    return datetime.strptime(date_string, format_string)


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