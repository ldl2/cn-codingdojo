from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key="sosecret"

@app.route('/')

def index():
    if 'gold' not in session:
        session['gold'] = 0
    return render_template('index.html', gold=session['gold'])

@app.route('/process_money', methods=['POST'])

def money():
    if request.form['building'] == 'farm':
        session['gold']=int(session['gold'])+random.randrange(10, 21)
    elif request.form['building'] == 'cave':
        session['gold']=int(session['gold'])+random.randrange(5, 11)
    elif request.form['building'] == 'house':
        session['gold']=int(session['gold'])+random.randrange(2, 6)
    elif request.form['building'] == 'casino':
        session['gold']=int(session['gold'])+random.randrange(-50, 51)
    return redirect('/')

app.run(debug=True)
