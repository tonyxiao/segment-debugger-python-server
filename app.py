import analytics
import json
import os
from flask import Flask, request, abort
app = Flask(__name__)

@app.route('/api/identify', methods=['POST'])
def identify():
    write_key = request.args.get('writeKey')
    params = request.get_json(True)
    
    # Shouldn't have any concurrency issue since we are not multi-threading here
    analytics.write_key = write_key
    analytics.identify(params['userId'], params['traits'])
    analytics.flush()
    
    return json.dumps({'status': 'success'})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

# analytics.write_key = 'dMCgkHYgAAhLeFYjG1uc46JLvohsWWRx'
# analytics.identify('019mr8mf4r', {
#     'email': 'john@example.com',
#     'name': 'John Smith',
#     'friends': 30
# })