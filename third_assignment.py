from flask import Flask

app = Flask(__name__)

@app.route('/content')
def read():
    f = open('files/words.txt', 'r')
    content = f.read()
    f.close()
    return content, 200

@app.route('/register')
def write():
    f = open('files/words.txt', 'w')
    f.write('Hello')
    f.close()
    return "success", 201


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=30000)