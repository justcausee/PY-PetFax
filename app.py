# # config
# from flask import Flask
# app = Flask(__name__)

# # index route
# @app.route('/')
# def index():
#     return 'Hello, this is Petfax!'

from petfax import create_app
app = create_app()