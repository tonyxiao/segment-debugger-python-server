import analytics
import os
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/api/identify')
def identify():
    write_key = request.args.get('writeKey')
    # Shouldn't have any concurrency issue since we are not multi-threading here
    analytics.write_key = write_key
    analytics.identify('019mr8mf4r', {
        'email': 'john@example.com',
        'name': 'John Smith',
        'friends': 30
    })
    analytics.flush()
    
    return 'Done'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

# analytics.write_key = 'dMCgkHYgAAhLeFYjG1uc46JLvohsWWRx'
# analytics.identify('019mr8mf4r', {
#     'email': 'john@example.com',
#     'name': 'John Smith',
#     'friends': 30
# })