from flask import Flask, render_template, request, redirect, url_for
from model.model import *
import datetime

app = Flask(__name__)

@app.route('/')
def To_do():
    create_table()
    tasks = get_tasks()
    return render_template('To_Do.html', tasks=tasks)

@app.route('/To_Do', methods=['POST'])
def tasks():
    task = request.form['task']
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    add_task(task, time)
    return redirect(url_for('To_do'))

@app.route('/delete', methods=['POST'])
def delete_task():
    task = request.form['task']
    delete(task)
    return redirect(url_for('To_do'))



if __name__ == '__main__':
    app.run(debug=True)