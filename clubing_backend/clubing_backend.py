# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Resource, Api
from .exercise_manager import ExerciseManager

app = Flask(__name__)
api = Api(app)

api.add_resource(ExerciseManager, '/exercise')
