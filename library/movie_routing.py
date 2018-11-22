from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def Genre():
  return render_template('routing/Genre-List.html')

@app.route('/Action')
def action():
  return render_template('routing/Action.html')

@app.route('/Horror')
def horror():
  return render_template('routing/Horror.html')

@app.route('/Sci-Fi')
def scifi():
  return render_template('routing/Sci-Fi.html')

