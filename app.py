import os 
from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hello Folks. My awesome application message: ' + os.environ.get('MESSAGE')

app.run(debug=True, host='0.0.0.0', port=5000)