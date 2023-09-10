from flask import Flask
from flask import request
from flask import jsonify
import datetime
import json

app = Flask(__name__)

@app.route('/', methods=['GET']) #Root URL is the first page
def run():
    try: 
        #Some variables that go into the JSON output
        slack_name = request.args.get('candidate', 'Slimpriest')
        track = request.args.get('track', 'Backend Developer')
        current_day =  datetime.date.today().strftime('%A')
        utc_time = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%Sz')
        #github_file =
        #github_repo =     
        
        #JSON output at endpoint
        output = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": utc_time,
            "track": track,
            "github_file_url": "URL to be inserted later",
            "github_repo_url": "URL to be inserted later",
            "status_code": "200"
        }

        return json.dumps(output, indent=None, sort_keys=False), 200, {'Content-Type': 'application/json'} #return JSON output

    except Exception as e:
        return jsonify({"error": str(e)}), 400 #Error Handling

if __name__ == '__main__':
    app.run(debug=True)