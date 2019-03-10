from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import DataInput

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


@app.route('/data', methods=['GET', 'POST'])
def data():
    form = DataInput()
    if form.validate_on_submit():
        flash('Data input for record {}'.format(
            form.record_id.data))
        return redirect(url_for('index'))
    return render_template('data.html', title='Data Input', form=form)

