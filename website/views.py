from flask import Blueprint, render_template, request,send_from_directory, flash, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
from . import db

views = Blueprint('views', __name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = 'website/static/uploads/'

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            flash('Image Caption Generated and Displayed Below!')
            return redirect(url_for('views.home', filename=filename))
        else:
            flash('Allowed image types are - png, jpg, jpeg, gif')

    filename = request.args.get('filename', None)
    return render_template('home.html', filename=filename)
    

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@views.route('/uploads/<filename>')
def display_image(filename):
    return send_from_directory('static/uploads', filename)
