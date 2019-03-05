from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    entity = {'entity_name': 'Python & Flask Demo App'}
    records = [
        {
            'record_id': {'id': '01'},
            'text': 'This is record 01!'
        },
        {
            'record_id': {'id': '02'},
            'text': 'This is record 02!'
        }
    ]
    return render_template('index.html', title='Home', entity=entity, records=records)

