from flask import Flask, render_template, request
import os

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
	return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
	directory = os.path.join(APP_ROOT, 'static/')

	if not os.path.isdir(directory):
		os.mkdir(directory)
	else:
		print('Directory exist: {}'.format(directory))

	for upload in request.files.getlist('file'):
		filename = upload.filename
		destination = "/".join([directory, filename])
		upload.save(destination)

	return render_template('complete.html', image_name=filename)

# Display image after upload
@app.route('/gallery')
def get_gallery():
	image_names = os.listdir('./static')
	print(image_names)
	return render_template('gallery.html', image_names=image_names)


if __name__ == '__main__':
	app.run(debug=True)