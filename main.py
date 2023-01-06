from flask import Flask, render_template,request
from distance import find_distance
import os
# picFolder = os.path.join('static', 'img')
# print(picFolder)
app = Flask(__name__)
app.debug = True
app.config.update(
    SESSION_COOKIE_NAME = 'session_distcal',
    SESSION_COOKIE_PATH = '/distcal/'
)
# app.config['UPLOAD_FOLDER'] = picFolder
# pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'map.png')
# print(pic1)
@app.route('/test')
def hello():
    print('This will be printed to the terminal')
    return 'Hello, World!'
@app.route('/')
def form():
    
    return render_template('form.html')

@app.route('/', methods=['POST'])
def handle_form():
    input1 = request.form['input1']
    input2 = request.form['input2']
    result = find_distance(input1, input2)
    print(f'input1: {input1} input2: {input2}')
    return render_template('result.html',result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=18100)