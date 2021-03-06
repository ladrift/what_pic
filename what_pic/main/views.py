# -*- coding: utf-8 -*-
import os
from flask import render_template, session, url_for, \
        current_app, redirect, send_from_directory, \
        request, jsonify
from werkzeug import secure_filename
import pinyin

from . import main
from ..cloud_sight_yzy import CloudImage

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

LOCALE = 'en_US'
LANG = 'en_US'

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/upload', methods = ['POST'])
def upload():
    if request.method == 'POST':
        file_val = request.files['file']
        # print('filename:', file_val.filename)
        if file_val and allowed_file(file_val.filename):
            ascii_name = pinyin.get(file_val.filename)
            filename = secure_filename(ascii_name)
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file_val.save(file_path)

            # cloud_sight 
            try:
                cloud_img = CloudImage(file=open(file_path, 'rb'), locale=LOCALE, lang=LANG)
            except:
                return jsonify(type='mistake', content=None)

            try:
                os.remove(file_path)
            except:
                print('Remove failed. file not found.')
            if cloud_img:
                result = cloud_img.result()
                if result:
                    # print('result is', result.encode('utf-8'))
                    return jsonify(type='result', content=result)
                else:
                    print('result is None')
                    return jsonify(type='mistake', content=None)
            else:
                print('cloud_img is None')
                return jsonify(type='mistake', content=None)

@main.route('/_url_submit')
def url_submit():
    if request.args.get('type') == 'url':
        url = request.args.get('content')
        if url:
            cloud_img = CloudImage(url=url, locale=LOCALE, lang=LANG)
            if cloud_img:
                result = cloud_img.result()
                if result:
                    return jsonify(content=result, type='result')
                else:
                    print('result is None')
                    return jsonify(content=None, type='mistake')
            else:
                print('cloud_img is None')
                return jsonify(content=None, type='mistake')
        else:
            print('url is None')
            return jsonify(content=None, type='mistake')
    else:
        print('type is not `url`')
        return jsonify(content=None, type='mistake')


@main.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                                filename)
