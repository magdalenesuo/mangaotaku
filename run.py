#!/usr/bin/python
# coding: utf-8
""" Filename:     run.py
    Purpose:      This file runs the Flask application service
    Requirements: Flask
"""
from webapp import app

if __name__ == '__main__':
    app.run(debug=True)


