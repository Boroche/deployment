from flask import Flask
 
app = Flask(__name__)
 
@app.route('/hello')
def hello():
    return 'Hello World'

def add(x):
    return x+1


app.run(host='localhost', port=5000)
