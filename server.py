from flask import Flask, render_template, redirect, session, url_for
app = Flask(__name__)    

app.config['SECRET_KEY'] = '0f064a216ea7'

@app.route ('/')
@app.route('/home')           
def home():
    if 'plus' not in session:
        session["plus"] = 0
    else:
        session["plus"] += 1
    return render_template('home.html')

@app.route('/destroy')          
def destroy():
    session.clear()
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)    

