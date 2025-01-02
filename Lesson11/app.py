from flask import Flask, render_template, request
import time
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/get_time')
def get_time():
    time_now = datetime.now().strftime("%Y-%m-%D %H:%M:%S")
    return {'time': time_now}

@app.route('/')
def clock():
    return render_template('index.html')

@app.route('/<filename>', methods=['GET'])
def static_file(filename):
    return app.send_static_file(filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)