from analytics import Client
import json
import os
from flask import Flask, request, abort
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/identify', methods=['POST'])
def identify():
    write_key = request.args.get('writeKey')
    params = request.get_json(True)
    
    # Shouldn't have any concurrency issue since we are not multi-threading here
    analytics = Client(write_key)
    analytics.identify(params['userId'], params['traits'])
    analytics.flush()
    
    return json.dumps({'status': 'success'})
    
@app.route('/api/track', methods=['POST'])
def track():
    write_key = request.args.get('writeKey')
    params = request.get_json(True)
    
    analytics = Client(write_key)
    analytics.track(params['userId'], params['event'], params['properties'])
    analytics.flush()
    
    return json.dumps({'status': 'success'})
    
@app.route('/api/alias', methods=['POST'])
def alias():
    write_key = request.args.get('writeKey')
    params = request.get_json(True)
    
    analytics = Client(write_key)
    analytics.alias(params['previousId'], params['userId'])
    analytics.flush()
    
    return json.dumps({'status': 'success'})
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
