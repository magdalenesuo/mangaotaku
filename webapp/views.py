#!/usr/bin/python
# coding: utf-8

import flask
import manga_scrape
from webapp import app
import re
import shutil
import os

# importing application wide parameters and global variables that have been
# defined in __init__.py

@app.route('/', methods=('GET','POST'))
def webapp():
	url=""
	pages=""
	folder=""
	filename=""
	if flask.request.method=='POST':
		url = flask.request.form.get('url')
		pages = flask.request.form.get('pages')
		folder=re.split(r"/", url)[3] + "_"+re.split(r"/", url)[4]
		manga_scrape.main(url, folder, int(pages))
		os.path.dirname(os.path.abspath(__file__))
		directory_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../" + folder)
		shutil.make_archive(folder, 'zip', directory_name)
	return flask.render_template('index.html', url=url, 
					pages=pages, filename=folder+".zip")

@app.route('/download/<path:filename>')
def download(filename):
	download_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../")
	return flask.send_from_directory(directory=download_folder, filename=filename) 

@app.route('/about/')
def about():
    return flask.render_template('about.html')

@app.route('/contact/')
def contact():
    return flask.render_template('contact.html', yo="pp")
