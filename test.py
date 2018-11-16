from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello, World!"


@app.route('/user/<username>')
def userpage(username):
    user_data = {
        'full_name': 'Pavel Okopnyi',
        'homepage': 'https://www.uib.no/en/persons/Pavel.Okopnyi'
    }
    return render_template('page01.html', user = username, user_data = user_data)




app.run('83.220.168.38', port=5001)
