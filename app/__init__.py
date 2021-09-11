from flask import Flask, app
from flask.scaffold import F

#Initializing application
app = Flask(__name__)

from app import views