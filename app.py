from flask import Flask, jsonify, request

from datetime import datetime

app = Flask(__name__)

@app.route('/api', methods= ['GET'])
def show():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    
    
    current_day = datetime.today().strftime("%A")
    
    utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    return jsonify ({
        "slack_name" : slack_name,
        "current_day" : current_day,
        "utc_time" : utc_time,
        "track" :track,
        "github_file_url" : "https://github.com/daniyamz/finishedpoint/blob/master/app.py",
        "github_repo_url" : "https://github.com/daniyamz/finishedpoint/tree/master",
        "status_code" : 200
    })
    
if __name__ == 'main':
    app.run()   
    