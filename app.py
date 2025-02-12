import os 
from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hello Pierre, Hakim, Remi and CoP Devops: ' + os.environ.get('MESSAGE')

app.run(debug=True, host='0.0.0.0', port=5000)