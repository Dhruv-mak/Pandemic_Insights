from flask import Blueprint, jsonify
from db import db_obj
api = Blueprint('api', __name__)
from sqlalchemy import text

@api.route("/")
def hello():
    result = db_obj.execute_raw("select * from aqi")
    # Fetch the column names from the result set
    column_names = [column[0] for column in result.cursor.description]

    # Convert the query result to a list of dictionaries
    result_dict = [dict(zip(column_names, row)) for row in result]

    return jsonify(result_dict)