from flask import Flask
from flask import request
from flask import jsonify
import datetime
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def run():
    try:
        #JSON output at endpoint
        output = {
            "slack_name": request.args.get('slack_name', 'Slimpriest'),
            "current_day": datetime.date.today().strftime('%A'),
            "utc_time": datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%Sz'),
            "track": request.args.get('track', 'Backend Developer'),
            "github_file_url": "https://github.com/Samttop/Endpoint_HNGx_Task1/blob/main/EndpointTask1.py",
            "github_repo_url": "https://github.com/Samttop/Endpoint_HNGx_Task1",
            "status_code": "200"
        }

        return json.dumps(output, indent=None, sort_keys=False), 200, {'Content-Type': 'application/json'} #return JSON output

    except Exception as e:
        return jsonify({"error": str(e)}), 400 #Error Handling
