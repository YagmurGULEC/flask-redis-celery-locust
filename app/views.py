from flask import Blueprint,render_template,redirect,request,url_for
from .tasks import add,upload_task

from flask import current_app
import os

import base64
import io
from flask import current_app
from .utils import process_file_to_stream
main=Blueprint('main',__name__)




@main.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            filestream=process_file_to_stream(uploaded_file)
            task = upload_task.delay(filestream,current_app.config['UPLOAD_PATH'])
            return redirect(url_for('main.status',task_id=task.id))
        else:
            return 'No file uploaded'

    else:

        return render_template('index.html')

@main.route('/add/<int:x>/<int:y>')
def add_link(x,y):
    task=add.delay(x,y)
    return redirect(url_for('main.status',task_id=task.id))

@main.route('/status/<task_id>')
def status(task_id):
    task=upload_task.AsyncResult(task_id)
    return task.state