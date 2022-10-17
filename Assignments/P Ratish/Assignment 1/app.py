from flask import *
app = Flask(__name__)
app.secret_key = 'super secret key'
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'GET':
      user = request.args.get('uname')
      password = request.args.get('passw')
      gender = request.args.get('gender')
      interest = request.args.get('interest')
      degree = request.args.get('degree')
      if user == '' or password == '' or gender == '' or interest == '' or degree == '':
         flash("please enter all the fields")
         return render_template('login.html')  
      return render_template('success.html', user = user, password = password, gender = gender, interest = interest, degree = degree)

if __name__ == '__main__':
   app.config
   app.run(debug = True)