from flask import Flask, render_template, json, request, jsonify,redirect,url_for
from mainp import sudo_main
import solver
app = Flask(__name__)
sudo=0
@app.route('/',methods=['POST','GET'])
def main():
    return render_template('home.html')

@app.route('/readpic', methods = ['POST','GET'])
def get_pic_javascript_read():
	global sudo
	jsdata = request.form['javascript_data']
	imgcrop=jsdata[jsdata.index(',')+1:] #everything before the comma was added because of the post request
	import base64
	imgdata = base64.b64decode(imgcrop)
	filename = 'some_image.jpg'  #I assume you have a way of picking unique filenames
	with open(filename, 'wb') as f:
		f.write(imgdata)
	sudo=sudo_main('some_image.jpg')
	print sudo
	flat = [x for sublist in sudo for x in sublist] #convert 2d array sudo into 1d array flat
	return json.dumps(flat)

@app.route('/solve', methods = ['POST','GET'])
def solve():
	flag=solver.solve_sudoku(sudo)
	flat = [x for sublist in sudo for x in sublist] #convert 2d array sudo into 1d array flat
	return json.dumps(flat)
if __name__ == "__main__":
    app.run(debug="true")
