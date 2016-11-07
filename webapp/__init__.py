
#!/usr/bin/python
# coding: utf-8

from flask import Flask

app = Flask(__name__)

# application wide global variables and config parameters must be defined here
# (not in `run.py`) for being able to import them in the beginning of the
# views files but we can perfectly imagine a smarter config procedure

# The views modules that contain the application's routes are imported here
# Importing views modules MUST BE in the end of the file to avoid problems
# related to circular imports http://flask.pocoo.org/docs/patterns/packages
import webapp.views

