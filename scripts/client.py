#!/usr/bin/python3.6

import requests
import json

URL = "http://localhost"
port = ":8000"


def get_request():
    schemas = "/exercise"
    argument = "?type=badminton"

    full_url = URL + port + schemas + argument

    response = requests.get(full_url)

    return response


def post_request():
    schemas = "/exercise"

    full_url = URL + port + schemas

    headers = {
        'Content-Type': 'application/json; charset=utf-8'
    }

    data = {
        "owner": "심준열",
        "type": "badminton",
        "location": "seoul",
        "minimum_personnel": 2,
        "maximum_personnel": 4,
    }

    res = requests.post(full_url, headers=headers, data=json.dumps(data))

    return res


if __name__ == '__main__':
    print(post_request())
