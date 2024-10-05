from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB client setup
client = MongoClient('mongodb://localhost:27017/')
db = client.survey_db
collection = db.user_data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_data = {
            'age': request.form['age'],
            'gender': request.form['gender'],
            'total_income': request.form['total_income'],
            'expenses': {
                'utilities': request.form['utilities'],
                'entertainment': request.form['entertainment'],
                'school_fees': request.form['school_fees'],
                'shopping': request.form['shopping'],
                'healthcare': request.form['healthcare']
            }
        }
        collection.insert_one(user_data)
        return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
