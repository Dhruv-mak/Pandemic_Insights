import click
from flask import Flask, Blueprint
from flask.cli import with_appcontext, cli
from db import db_obj
import os
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
    HDI,
    Inequality,
)
import csv
import datetime

cli_bp = Blueprint("table_master", __name__)


def populate_table_generic(table_name, file_name, record_creator):
    exists = db_obj.check_table_exists(table_name)
    if not exists:
        db_obj.create_table(table_name)
        click.echo(f"Table {table_name} created")
    else:
        click.echo(f"Table {table_name} already exists")

    with open(os.path.join("data", file_name)) as f:
        reader = csv.reader(f)
        next(reader)
        session = db_obj.get_session()
        for row in reader:
            record = record_creator(row)
            session.add(record)
        session.commit()
        session.close()


@cli_bp.cli.command("populate-table")
@click.option('--table_name', default='all')
def cli_populate_table(table_name):
    """Populate table with data from csv file"""
    if table_name == "all":
        for table in ["Cases", "Mortality", "Population", "Vaccination", "StringencyIndex", "Hospitalization", "Testing", "Parameters", "Emissions"]:
            populate_table(table)
    else:
        populate_table(table_name)


def populate_table(table_name):
    if table_name == "Cases":
        populate_table_generic(
            table_name,
            "final_cases_deaths.csv",
            lambda row: Cases(
                date=datetime.datetime.strptime(row[0], "%m/%d/%Y").date(),
                location=row[1],
                new_cases=row[2],
                new_deaths=row[3],
            ),
        )
    elif table_name == "Mortality":
        populate_table_generic(
            table_name,
            "final_excess_mortality.csv",
            lambda row: Mortality(
                date=datetime.datetime.strptime(row[0], "%m/%d/%Y").date(),
                country=row[1],
                cumulative_estimated_daily_excess_death=row[2],
                cumulative_estimated_daily_excess_deaths_per_100k=row[3],
                estimated_daily_excess_deaths=row[4],
                estimated_daily_excess_deaths_per_100k=row[5],
            ),
        )
    elif table_name == "Population":
        populate_table_generic(
            table_name,
            "final_population.csv",
            lambda row: Population(country=row[0], population=row[1]),
        )
    elif table_name == "Vaccination":
        populate_table_generic(
            table_name,
            "final_vaccinations.csv",
            lambda row: Vaccination(
                date=datetime.datetime.strptime(row[0], "%m/%d/%Y").date(),
                location=row[1],
                total_vaccinations=row[2],
                people_vaccinated=row[3],
                daily_vaccinations=row[4],
                daily_people_vaccinated=row[5],
            ),
        )
    elif table_name == "StringencyIndex":
        populate_table_generic(
            table_name,
            "final_data_si.csv",
            lambda row: StringencyIndex(
                date=datetime.datetime.strptime(row[0], "%m/%d/%Y").date(),
                country=row[1],
                StringencyIndex_Avg=row[2],
            ),
        )
    elif table_name == "Hospitalization":
        populate_table_generic(
            table_name,
            "final_hospitalization.csv",
            lambda row: Hospitalization(
                date=datetime.datetime.strptime(row[0], "%Y-%m-%d").date(),
                country=row[1],
                daily_hospital_occupancy=row[2],
                daily_icu_occupancy=row[3],
            ),
        )
    elif table_name == "Testing":
        populate_table_generic(
            table_name,
            "final_testing.csv",
            lambda row: Testing(
                date=datetime.datetime.strptime(row[0], "%Y-%m-%d").date(),
                country=row[1],
                new_tests_smoothed=row[2],
            ),
        )
    elif table_name == "Parameters":
        populate_table_generic(
            table_name,
            "final_parameters.csv",
            lambda row: Parameters(
                country=row[0],
                gdp_per_capita=row[1],
                cardiovasc_death_rate=row[2],
                diabetes_prevalence=row[3],
                hospital_beds_per_thousand=row[4],
            ),
        )
    elif table_name == "Emissions":
        populate_table_generic(
            table_name,
            "final_emission.csv",
            lambda row: Emissions(
                country=row[0], 
                year=row[1],
                total_emissions=row[2],
                co2_emission_coal=row[3],
                co2_emission_oil=row[4],
                co2_emission_gas=row[5],
                co2_emission_cement=row[6],
                co2_emission_flaring=row[7],
                co2_emission_per_capita=row[8],
            ),
        )
    elif table_name == "HDI":
        populate_table_generic(
            table_name,
            "final_hdi.csv",
            lambda row: HDI(
                year = row[0],
                country = row[1],
                le = float(row[2]) if row[2] != '' else None,
                eys = float(row[3]) if row[3] != '' else None,
                mys = float(row[4]) if row[4] != '' else None,
                gnipc = float(row[5]) if row[5] != '' else None
            ),
        )
    elif table_name == "Inequality":
        populate_table_generic(
            table_name,
            "final_inequality.csv",
            lambda row: Inequality(
                year = row[0],
                country = row[1],
                abr = float(row[2]) if row[2] != '' else None,
                mmr = float(row[3]) if row[3] != '' else None,
                prf = float(row[4]) if row[4] != '' else None,
                sef = float(row[5]) if row[5] != '' else None,
                prm = float(row[6]) if row[6] != '' else None,
                sem = float(row[7]) if row[7] != '' else None,
                lfprf = float(row[8]) if row[8] != '' else None,
                lfprm = float(row[9]) if row[9] != '' else None
            )
        )
    else:
        click.echo(f"Table {table_name} does not exist")


@cli_bp.cli.command("grant-access") 
@click.option('--table_name', default='all')
@click.option('--user_name', default='all')
def grant_access(table_name, user_name):
    if table_name == "all":
        table_list =  [
            "Cases",
            "Mortality",
            "Population",
            "Vaccination",
            "StringencyIndex",
            "Hospitalization",
            "Testing",
            "Parameters",
            "Emissions",
        ]
    else:
        table_list = [table_name]
    if user_name == "all":
        user_list = ["VAHER", "SAKSHI.PANDEY", "VISHALPRAKASH"]
    else:
        user_list = [user_name]
    for table in table_list:
        for user in user_list:
            if db_obj.check_table_exists(table):
                db_obj.grant_access(table, user)
                click.echo(f"Access granted to {user} on {table}")
            else:
                click.echo(f"Table {table} does not exist")
