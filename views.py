from __main__ import app
from flask import render_template


@app.route('/upload_file', methods=['GET'])
def test():
    return render_template('upload_file.html')

