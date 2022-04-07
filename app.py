from flask import Flask, render_template, request, url_for, redirect
import text2emotion as te
from heapq import nlargest

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':

        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        phone = request.form['phone']
        feedback = request.form['feedback']

        feeling = te.get_emotion(feedback)
        emotion = nlargest(1, feeling, key=feeling.get)

        context = {
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'phone': phone,
            'emotion': emotion
        }
        return render_template('result.html', **context)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)