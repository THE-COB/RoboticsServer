import os
from flask import Flask, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import time

c = str(time.clock())
UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'apk'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		# check if the post request has the file part
		if 'file' not in request.files:
			print('No file part')
			return redirect(request.url)
		file = request.files['file']
		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':
			print('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			os.system("mv uploads/newest.apk uploads/olds/"+c+".apk")
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], "newest.apk"))
			return redirect(url_for('upload_file', filename=filename))
	f = open("index.html")
	iStr = f.read()
	f.close()
	return iStr

@app.route("/get-file")
def download():
	return send_file("./uploads/newest.apk", as_attachment=True)