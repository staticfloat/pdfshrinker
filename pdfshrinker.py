#!/usr/bin/env python

import tempfile, os, shutil
from subprocess import Popen, PIPE, STDOUT
from flask import Flask, request, Response, send_from_directory, jsonify
from werkzeug import secure_filename
app = Flask(__name__)

# This is where we'll store uploaded .pdf files
tmpdir = tempfile.mkdtemp()

def allowed_file(filename):
    return filename[-4:].lower() == '.pdf'

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['pdf_file']
        if f and allowed_file(f.filename):
            # Sanitize input filename, then write the .pdf file out to a local file
            filename = secure_filename(f.filename)
            f.save(os.path.join(tmpdir, filename))

            # Convert it to a smaller .pdf file using `gs`
            small_filename = filename[:-4] + '_small.pdf'
            p = Popen(['gs', '-o', small_filename, '-sDEVICE=pdfwrite',
                        '-dPDFSETTINGS=/prepress', '-dFastWebView=true',
                        '-dColorImageResolution=300', '-dGrayImageResolution=300',
                        '-dMonoImageResolution=300', '-f', filename], cwd=tmpdir)
            p.wait()

            return jsonify({'download_url':'/download/'+small_filename})

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(tmpdir, secure_filename(filename), as_attachment=True)

try:
    if __name__ == "__main__":
        app.run(port=5000)
finally:
    shutil.rmtree(tmpdir)
