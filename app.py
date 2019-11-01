from flask import Flask, request, render_template
app = Flask(__name__)

from commons import get_tensor
from inference import get_blood_type

@app.route('/', methods=['GET', 'POST'])
def hello_world():
	if request.method == 'GET':
		return render_template('index.html', value='hi')
	if request.method == 'POST':
		print(request.files)
		if 'file' not in request.files:
			print('file not uploaded')
			return
		file = request.files['file']
		image = file.read()
		category, blood_type = get_blood_type(image_bytes=image)
		get_blood_type(image_bytes=image)
		tensor = get_tensor(image_bytes=image)
		print(get_tensor(image_bytes=image))
		return render_template('result.html', blood=blood_type, category=category)

if __name__ == '__main__':
	app.run(debug=True)