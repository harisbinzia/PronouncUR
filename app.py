#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os, uuid, codecs
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename
import tensorflow as tf
import unicodedata
from g2p import G2PModel
import re

UPLOAD_FOLDER = 'uploads'
DOWNLOAD_FOLDER = 'downloads'
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
g2p_model = G2PModel("itudict")
g2p_model.load_decode_model()

spaceregex = re.compile("\s*");

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graphemes')
def graphemes():
    return render_template('graphemes.html')

@app.route('/phonemes')
def phonemes():
    return render_template('phonemes.html')

@app.route('/download/<filename>')
def download(filename):
    return render_template('download.html', filename=filename)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(url_for('index'))
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return redirect(url_for('index'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            fname = str(uuid.uuid4().hex)
            iname = fname +'.txt'
            oname = fname +'.txt'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], iname))
            temp_lines = None
            temp_lines = codecs.open(os.path.join(app.config['UPLOAD_FOLDER'], iname), "r", "utf-8").readlines()
            decode_lines = list()
            for i in temp_lines:
                decode_lines.append(unicodedata.normalize('NFC',i))
            output_file = None
            output_file = codecs.open(os.path.join(app.config['DOWNLOAD_FOLDER'], oname), "w", "utf-8")
            g2p_model.decode(decode_lines, output_file)
            return redirect(url_for('download', filename=oname))
    return redirect(url_for('index'))

@app.route('/g2p',methods=['POST'])
def convert():
    text = spaceregex.split(request.form['text'].replace(u'۔',' '))
    out = g2p_model.decode(text)
    return '\n'.join(out);

@app.route('/downloads/<filename>')
def download_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'],
                               filename, as_attachment=True)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("8080"),threaded=True)
