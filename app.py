
from flask import Flask #import main Flask class

app = Flask(__name__) #create the Flask app

@app.route("/")
def hello():
    return "Hello World!"

if __name__ =='__main__':
    app.run(debug='true',port=5000) #run app in debug mode on port 5000
