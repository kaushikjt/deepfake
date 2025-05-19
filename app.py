from flask import Flask, render_template, request, jsonify
import os
from utils.compare import is_match

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/input'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    ftype = request.form['type']
    fpath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(fpath)

    print(f"[INFO] Uploaded: {file.filename}, Type: {ftype}")
    result = is_match(fpath, ftype)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
