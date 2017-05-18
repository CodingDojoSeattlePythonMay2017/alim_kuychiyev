from flask import Flask, render_template,request,redirect,flash,session

app = Flask(__name__)
app.secret_key = 'secret'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['post'])
def result():

    if len(request.form['name']) < 1:
        flash('This Name Field cannot be empty!')
        return redirect('/')
    if len(request.form['comment']) < 1:
        flash('This Comment Field cannot be empty!')
        return redirect('/')
    elif len(request.form['comment']) > 150:
        flash('comment can only be 150 characters')
        return redirect('/')

    return render_template('result.html', name = request.form['name'], location =request.form['location'],language=request.form['language'],comment=request.form['comment'])

app.run(debug=True)
