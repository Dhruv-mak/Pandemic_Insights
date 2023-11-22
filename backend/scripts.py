import click
from flask import Flask, Blueprint
from flask.cli import with_appcontext, cli
from db import db_obj
import os
from models import AQI, Cases, Mortality, Population, Vaccination, StringencyIndex
import csv

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
            record = Mortality(
                date=row[0],
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
            record = Cases(
                date=row[0],
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
            record = Vaccination(
                date=row[0],
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
            record = StringencyIndex(
                date=row[0],
                country=row[1],
                StringencyIndex_Avg=row[2]
            )
            session.add(record)
        session.commit()
        session.close()