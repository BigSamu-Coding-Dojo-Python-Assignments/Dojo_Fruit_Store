from flask import Flask, render_template, request, redirect, session
from datetime import datetime
app = Flask(__name__) 
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security 

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['GET','POST'])         
def checkout():
    if request.method == 'POST':
        fruit_count = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
        fruits = {
            'sb': request.form['strawberry'],
            'rb': request.form['raspberry'],
            'ap': request.form['apple'],
            'fn': request.form['first_name'],
            'ln': request.form['last_name'],
            'sid': request.form['student_id'],
            'fc': fruit_count,
            'order_date': datetime.today().strftime('%B %d' + ' at ' + ' %I:%M:%S %p')
        }
        session['fruits'] = fruits
        print("Charging {} {} for {} fruits".format(request.form['first_name'], request.form['last_name'], fruit_count))
        return redirect("/checkout")
        
    print(session['fruits'])
    return render_template("checkout.html", deli_fruits=session['fruits'])

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    