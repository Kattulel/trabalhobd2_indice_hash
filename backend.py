from flask import Flask, render_template, request, redirect, url_for, abort, jsonify
from werkzeug.utils import secure_filename
import os
import sys
# problema com o arquivo grande
sys.setrecursionlimit(3000)
app = Flask(__name__)
control = None

app.config['UPLOAD_PATH'] = 'files'

@app.route('/start', methods=['POST'])
def upload_file():
    global control
    uploaded_file = request.files['file']
    bucket_size = request.form.get("bucket_size")
    page_size = request.form.get("page_size")
    f = open("globals.py", "w")
    f.write(f'bucket_size={bucket_size}\npage_size={page_size}')
    f.close()
    filename = secure_filename(uploaded_file.filename)
    file = None
    if filename != '':
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        file = os.path.join(app.config['UPLOAD_PATH'], filename)

    if file is not None:
        from control import Control
        control = Control()
        control.readfile(file)
    return jsonify(status="ok")

@app.route('/info', methods=['GET'])
def get_info():
    if control is None:
        return jsonify(status="error")
    return jsonify(control.get_info())

@app.route('/search', methods=['POST'])
def search():
    if control is None:
        return jsonify(status="error")
    query = request.args.get('query')
    steps = control.search(query)[0]
    return jsonify(custo=steps)

@app.route('/coisa', methods=['POST'])
def coisa():
    return request.get_json()

if __name__ == '__main__':
    app.run(debug=True)
