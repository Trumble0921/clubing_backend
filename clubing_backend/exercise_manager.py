import json
from flask import jsonify, request
from flask_restful import Resource, abort, reqparse
from datetime import datetime, timezone

from .database import Database
from .json_encoder import JSONEncoder
# Todo Make abort decorator when invalid request called. please use flask's abort


class ExerciseManager(Resource):

    def __init__(self):
        self.database_instance = Database()

    # return all exercise_db
    def get(self):
        parser = reqparse.RequestParser()

        parse_list = [
            {"type": str},
            {"member_id": str}
        ]
        for parse in parse_list:
            parser.add_argument(parse, type=type(parse))
        request_parameter = parser.parse_args()

        parsing_data = self.database_instance.get_attribute("exercise_db", "exercise", request_parameter)
        parsing_data = json.dumps(parsing_data[0], cls=JSONEncoder)

        return jsonify(parsing_data[0])

    # register new exercise_db
    def post(self):
        now_utc = datetime.utcnow()
        now_utc = now_utc.replace(tzinfo=timezone.utc)

        request_data = request.get_json(silent=True)
        remap_exercise = request_data
        remap_exercise["status"] = "recruiting"
        remap_exercise["member"] = [remap_exercise["owner"]]
        remap_exercise["created_time"] = now_utc
        remap_exercise["updated_time"] = now_utc
        remap_exercise["description"] = None

        self.database_instance.insert_attribute("exercise_db", "exercise", remap_exercise)
        return {"msg": "ok"}, 200

    # delete specific exercise_db
    def delete(self):
        return 200
