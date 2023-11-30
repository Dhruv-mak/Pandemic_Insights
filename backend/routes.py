from flask import Blueprint, jsonify, request
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
    HDI,
    Inequality,
)
from graph_utility import (
    get_line_graph_query1,
    get_stacked_area_chart,
    get_percentile_graph_query1,
    new_cases_smoothed_query1,
    get_positivity_rate_color_coded_scatter,
    get_global_vs_country_trend_line_graph,
    get_line_graph_new_deaths_smoothed,
    get_interaction_graph,
    get_metric_rank_graph,
    get_line_graph,
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
    elif query_index == 2:
        table1 = session.query(Emissions.country.distinct()).order_by(Emissions.country)
        intersection = table1
    elif query_index == 3:
        table1 = session.query(Cases.location)
        table2 = session.query(Parameters.country)
        intersection = table1.intersect(table2)
    elif query_index == 4:
        intersection = session.query(HDI.country.distinct()).order_by(HDI.country)
    elif query_index == 5:
        intersection = session.query(Inequality.country.distinct()).order_by(Inequality.country)
    result = intersection.all()
    result = [r[0] for r in result]
    session.close()
    return jsonify(result)


@api.route("/get_query/<int:query_index>/<string:country_list>")
def get_query(query_index, country_list):
    if query_index == 1:
        country_list = country_list.split(",")
        country_list = ",".join([f"'{country}'" for country in country_list])
        with open("queries/query1.sql", "r") as f:
            query = f.read()
        query = query.replace(":country_list", country_list)
        data = pd.read_sql(query, db_obj.engine)
        data["date"] = pd.to_datetime(data["date"], format="%d-%b-%y")

        graphs = []
        graphs.append(get_line_graph_query1(data))
        graphs.append(get_stacked_area_chart(data))
        # graphs.append(get_percentile_graph_query1(data))
        graphs.append(new_cases_smoothed_query1(data))
        graphs.append(get_positivity_rate_color_coded_scatter(data))
        
        return json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    elif query_index == 2:
        emmission_type = request.args.get("emission_type")
        country_list += ",Global"
        country_list = country_list.split(",")
        country_list = ",".join([f"'{country}'" for country in country_list])
        with open("queries/query2.sql", "r") as f:
            query = f.read()
        query = query.replace(":country_list", country_list)
        data = pd.read_sql(query, db_obj.engine)
        data["date"] = pd.to_datetime(data["year"])
        
        graphs = []
        graphs.append(get_global_vs_country_trend_line_graph(data, emmission_type))
        return json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    elif query_index == 3:
        interaction_type = request.args.get("interaction_type")
        country_list = country_list.split(",")
        country_list = ",".join([f"'{country}'" for country in country_list])
        with open("queries/query3.sql", "r") as f:
            query = f.read()
        query = query.replace(":country_list", country_list)
        data = pd.read_sql(query, db_obj.engine)
        data["date"] = pd.to_datetime(data["date"], format="%d-%b-%y")
        
        graphs = []
        graphs.append(get_line_graph_new_deaths_smoothed(data))
        if len(interaction_type) != 0:
            graphs.append(get_interaction_graph(data, interaction_type))
            if interaction_type == "hospital_beds_death_interaction":
                graphs.append(get_metric_rank_graph(data, "hostpital_beds"))
            else:
                graphs.append(get_metric_rank_graph(data, interaction_type.split("_")[0]))
        return json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    elif query_index == 4:
        country_list = country_list.split(",")
        country_list = ",".join([f"'{country}'" for country in country_list])
        with open("queries/query4.sql", "r") as f:
            query = f.read()
        query = query.replace(":country_list", country_list)
        data = pd.read_sql(query, db_obj.engine)
        graphs = []
        graphs.append(get_line_graph(data, "hdi"))
        return json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    elif query_index == 5:
        country_list = country_list.split(",")
        country_list = ",".join([f"'{country}'" for country in country_list])
        with open("queries/query5.sql", "r") as f:
            query = f.read()
        query = query.replace(":country_list", country_list)
        data = pd.read_sql(query, db_obj.engine)
        graphs = []
        graphs.append(get_line_graph(data, "gii"))
        return json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
        


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
    result += session.query(HDI).count()
    result += session.query(Inequality).count()
    session.close()
    return jsonify(result)