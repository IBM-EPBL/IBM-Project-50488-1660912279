import sys
sys.path.append('/workspace/python_db/dbconn.py')
from urllib import request
from flask import Flask,render_template,url_for

app = Flask(__name__)
@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/result",methods=['POST'])
def send_data():
    name=request.form['email']
    #dbconn.Insert_values()
    return "hello"
if __name__=="__main__":
    app.run(debug=True)