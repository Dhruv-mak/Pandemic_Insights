from flask import Blueprint, jsonify
from db import db_obj
from datetime import datetime

api = Blueprint("api", __name__)
from sqlalchemy import text, select
from models import (
    AQI,
    Cases,
    Mortality,
    Population,
    Vaccination,
    StringencyIndex,
    Hospitalization,
    Testing,
    Parameters,
    Emissions,
)


@api.route("/")
def hello():
    # result = db_obj.execute_raw('select * from "Population"')
    # # Fetch the column names from the result set
    # column_names = [column[0] for column in result.cursor.description]

    # # Convert the query result to a list of dictionaries
    # result_dict = [dict(zip(column_names, row)) for row in result]

    # return jsonify(result_dict)
    return "Hello World!"


@api.route("/get_countries/<int:query_index>")
def get_countries(query_index):
    session = db_obj.get_session()
    if query_index == 1:
        table1 = session.query(Cases.location)
        table2 = session.query(Population.country)
        table3 = session.query(Parameters.country)
        intersection = table1.intersect(table2).intersect(table3)
        result = intersection.all()
        result = [r[0] for r in result]
        session.close()
        return jsonify(result)


@api.route("/get_query/<int:query_index>/<string:country_list>")
def get_query(query_index, country_list):
    if query_index == 1:
        country_list = country_list.split(",")
        with open("queries/query1.sql", "r") as f:
            query = f.read()

        bind_vars = {f'country{i}': country for i, country in enumerate(country_list)}
        in_clause = ', '.join(f':country{i}' for i in range(len(country_list)))
        query = query.replace(':country_list', in_clause)
        result = db_obj.execute_raw(query, **bind_vars)
        column_names = [column[0] for column in result.cursor.description]
        result_dict = [dict(zip(column_names, row)) for row in result]
        for r in result_dict:
            r["date"] = r["date"].strftime("%Y-%m-%d")
        return jsonify(result_dict)
