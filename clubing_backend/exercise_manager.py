from flask import jsonify
from flask_restful import Resource, abort, reqparse

from .database import Database
# Todo Make abort decorator when invalid request called. please use flask's abort


class ExerciseManager(Resource):

    def __init__(self):
        self.database_instance = Database()

    # return all exercise
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str)
        parser.add_argument('member_id', type=str)
        request_parameter = parser.parse_args()

        parsing_data = self.database_instance.get_attribute(request_parameter)

        return parsing_data

    # register new exercise
    def post(self):

        return 200

    # delete specific exercise
    def delete(self):
        return 200
