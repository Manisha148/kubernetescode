# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Manisha Verma '
from flask import *
import os
import socket

app = Flask(__name__)

# app.config["Debug"] = True
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

    
if _name_ == '__main__':
    app.run()


PORT = int(os.environ.get("PORT", 9090))
if _name_ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=PORT)

if _name_ == "__main__":
  app.run(host='0.0.0.0', port=9090)
