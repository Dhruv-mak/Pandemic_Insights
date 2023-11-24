import click
from flask import Flask, Blueprint
from flask.cli import with_appcontext, cli
from db import db_obj
import os
from models import AQI, Cases, Mortality, Population, Vaccination, StringencyIndex, Hospitalization, Testing, Parameters
import csv
import datetime

cli_bp = Blueprint("table_master", __name__)


@cli_bp.cli.command("populate-table")
@click.argument("table_name")
def populate_table(table_name):
    # if table_name == "AQI":
    #     populate_aqi(table_name)args
    if table_name == "Cases":
        populate_cases(table_name)
    elif table_name == "Mortality":
        populate_mortality(table_name)
    elif table_name == "Population":
        populate_population(table_name)
    elif table_name == "Vaccination":
        populate_vaccination(table_name)
    elif table_name == "StringencyIndex":
        populate_stringency_index(table_name)
    elif table_name == "Testing":
        populate_testing(table_name)
    elif table_name == 'Hospitalization':
        populate_hospitalization(table_name)
    elif table_name == 'Parameters':
        populate_parameters(table_name)
        
@cli_bp.cli.command("grant-access")
@click.argument("table_name")
@click.argument("user_name")
def grant_access(table_name, user_name):
    db_obj.grant_access(table_name, user_name)

def populate_mortality(table_name):
    """Populate a table with some data"""
    exists = db_obj.check_table_exists(table_name)
    if not exists:
        db_obj.create_table(table_name)
    else:
        print(f"Table {table_name} already exists")
    
    with open(os.path.join("data/final_excess_mortality.csv")) as f:
        reader = csv.reader(f)
        next(reader)
        session = db_obj.get_session()
        for row in reader:
            # Convert the date string to a datetime.date object
            date = datetime.datetime.strptime(row[0], "%m/%d/%Y").date()
            record = Mortality(
                date=date,
                country=row[1],
                cumulative_estimated_daily_excess_death=row[2],
                cumulative_estimated_daily_excess_deaths_per_100k=row[3],
                estimated_daily_excess_deaths=row[4],
                estimated_daily_excess_deaths_per_100k=row[5]
            )
            session.add(record)
        session.commit()
        session.close()
    
        
def populate_cases(table_name):
    """Populate a table with some data"""
    # check if the table exists in the database
    # if not, create it
    # if yes, populate it with some data
    exists = db_obj.check_table_exists(table_name)
    if not exists:
        db_obj.create_table(table_name)
    else:
        click.echo(f"Table {table_name} already exists")
    
    with open(os.path.join("data/final_cases_deaths.csv")) as f:
        reader = csv.reader(f)
        next(reader)
        session = db_obj.get_session()
        for row in reader:
            # Convert the date string to a datetime.date object
            date = datetime.datetime.strptime(row[0], "%m/%d/%Y").date()
            record = Cases(
                date=date,
                location=row[1],
                new_cases=row[2],
                new_deaths=row[3]
            )
            session.add(record)
        session.commit()
        session.close()

def populate_population(table_name):
    """Populate a table with some data"""
    # check if the table exists in the database
    # if not, create it
    # if yes, populate it with some data
    exists = db_obj.check_table_exists(table_name)
    if not exists:
        db_obj.create_table(table_name)
        click.echo(f"Table {table_name} created")
    else:
        click.echo(f"Table {table_name} already exists")
    
    with open(os.path.join("data/final_population.csv")) as f:
        reader = csv.reader(f)
        next(reader)
        session = db_obj.get_session()
        for row in reader:
            record = Population(
                country=row[0],
                population=row[1]
            )
            session.add(record)
        session.commit()
        session.close()

def populate_vaccination(table_name):
    """Populate a table with some data"""
    # check if the table exists in the database
    # if not, create it
    # if yes, populate it with some data
    exists = db_obj.check_table_exists(table_name)
    if not exists:
        db_obj.create_table(table_name)
        click.echo(f"Table {table_name} created")
    else:
        click.echo(f"Table {table_name} already exists")
    
    with open(os.path.join("data/final_vaccinations.csv")) as f:
        reader = csv.reader(f)
        next(reader)
        session = db_obj.get_session()
        for row in reader:
            # Convert the date string to a datetime.date object
            date = datetime.datetime.strptime(row[0], "%m/%d/%Y").date()
            record = Vaccination(
                date=date,
                location=row[1],
                total_vaccinations=row[2],
                people_vaccinated=row[3],
                daily_vaccinations=row[4],
                daily_people_vaccinated=row[5]
            )
            session.add(record)
        session.commit()
        session.close()

def populate_stringency_index(table_name):
    """Populate a table with some data"""
    # check if the table exists in the database
    # if not, create it
    # if yes, populate it with some data
    exists = db_obj.check_table_exists(table_name)
    if not exists:
        db_obj.create_table(table_name)
        click.echo(f"Table {table_name} created")
    else:
        click.echo(f"Table {table_name} already exists")
    
    with open(os.path.join("data/final_data_si.csv")) as f:
        reader = csv.reader(f)
        next(reader)
        session = db_obj.get_session()
        for row in reader:
            # Convert the date string to a datetime.date object
            date = datetime.datetime.strptime(row[0], "%m/%d/%Y").date()
            record = StringencyIndex(
                date=date,
                country=row[1],
                StringencyIndex_Avg=row[2]
            )
            session.add(record)
        session.commit()
        session.close()
    
def populate_hospitalization(table_name):
    """Populate a table with some data"""
    # check if the table exists in the database
    # if not, create it
    # if yes, populate it with some data
    exists = db_obj.check_table_exists(table_name)
    if not exists:
        db_obj.create_table(table_name)
        click.echo(f"Table {table_name} created")
    else:
        click.echo(f"Table {table_name} already exists")
    
    with open(os.path.join("data/final_hospitalization.csv")) as f:
        reader = csv.reader(f)
        next(reader)
        session = db_obj.get_session()
        for row in reader:
            # Convert the date string to a datetime.date object
            date = datetime.datetime.strptime(row[0], "%Y-%m-%d").date()
            record = Hospitalization(
                date=date,
                country=row[1],
                daily_hospital_occupancy=row[2],
                daily_icu_occupancy=row[3]
            )
            session.add(record)
        session.commit()
        
        session.close()
        
def populate_testing(table_name):
    """Populate a table with some data"""
    # check if the table exists in the database
    # if not, create it
    # if yes, populate it with some data
    exists = db_obj.check_table_exists(table_name)
    if not exists:
        db_obj.create_table(table_name)
        click.echo(f"Table {table_name} created")
    else:
        click.echo(f"Table {table_name} already exists")
    
    with open(os.path.join("data/final_testing.csv")) as f:
        reader = csv.reader(f)
        next(reader)
        session = db_obj.get_session()
        for row in reader:
            # Convert the date string to a datetime.date object
            date = datetime.datetime.strptime(row[0], "%Y-%m-%d").date()
            record = Testing(
                date=date,
                country=row[1],
                new_tests_smoothed=row[2]
            )
            session.add(record)
        session.commit()
        session.close()

def populate_parameters(table_name):
    """Populate a table with some data"""
    # check if the table exists in the database
    # if not, create it
    # if yes, populate it with some data
    exists = db_obj.check_table_exists(table_name)
    if not exists:
        db_obj.create_table(table_name)
        click.echo(f"Table {table_name} created")
    else:
        click.echo(f"Table {table_name} already exists")
    
    with open(os.path.join("data/final_parameters.csv")) as f:
        reader = csv.reader(f)
        next(reader)
        session = db_obj.get_session()
        for row in reader:
            record = Parameters(
                country = row[0],
                gdp_per_capita = row[1],
                cardiovasc_death_rate = row[2],
                diabetes_prevalence = row[3]
            )
            session.add(record)
        session.commit()
        session.close()