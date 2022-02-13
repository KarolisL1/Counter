from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'count' not in session:
        print('key exists!')
        session['count'] = 1
    else:
        print("key 'key_name' does NOT exist")
        session['count'] += 1
    return render_template("index.html")


@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    