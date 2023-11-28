from flask import Blueprint, jsonify
from db import db_obj
from datetime import datetime
from plotly import graph_objs as go
from plotly import express as px
import plotly
import pandas as pd
import json
api = Blueprint("api", __name__)
from sqlalchemy import text, select
from models import (
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
    return "Hello World!"


@api.route("/get_countries/<int:query_index>")
def get_countries(query_index):
    session = db_obj.get_session()
    if query_index == 1:
        table1 = session.query(Cases.location)
        table2 = session.query(Testing.country)
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
        country_list = ','.join([f"'{country}'" for country in country_list])
        with open("queries/query1.sql", "r") as f:
            query = f.read()
        query = query.replace(':country_list', country_list)
        data = pd.read_sql(query, db_obj.engine)
        data['date'] = pd.to_datetime(data['date'], format='%d-%b-%y')

        fig = px.line(data, x='date', y='test_positivity_rate', color='country', 
                    title='Test Positivity Rate Over Time by Country')

        fig.update_layout(
            xaxis_title='Date',
            yaxis_title='Test Positivity Rate',
            xaxis=dict(showline=True, showgrid=False, showticklabels=True, linecolor='rgb(204, 204, 204)', linewidth=2, ticks='outside', tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)')),
            yaxis=dict(showgrid=False, zeroline=False, showline=False, showticklabels=True),
            autosize=True,
            margin=dict(autoexpand=True),
            showlegend=True,
            plot_bgcolor='white'
        )
        fig.show()
        graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graph_json
    
@api.route("/get_count")
def get_count():
    session = db_obj.get_session()
    result = session.query(Cases).count()
    result += session.query(Mortality).count()
    result += session.query(Population).count()
    result += session.query(Vaccination).count()
    result += session.query(StringencyIndex).count()
    result += session.query(Hospitalization).count()
    result += session.query(Testing).count()
    result += session.query(Parameters).count()
    result += session.query(Emissions).count()
    session.close()
    return jsonify(result)