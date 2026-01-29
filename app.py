from flask import Flask, jsonify, render_template
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/time')
def get_time():
    # Get current time from World Time API
    response = requests.get('http://worldtimeapi.org/api/timezone/Etc/UTC')
    data = response.json()
    current_time = datetime.fromisoformat(data['datetime'].replace('Z', '+00:00'))
    return jsonify({
        'utc_time': current_time.isoformat(),
        'timezone': data['timezone'],
        'day_of_week': current_time.strftime('%A'),
        'day_of_year': current_time.strftime('%j')
    })

if __name__ == '__main__':
    app.run(debug=True)
