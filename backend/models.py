from db import db_obj
from sqlalchemy import text, PrimaryKeyConstraint, String, Float, Integer, DATE
BASE = db_obj.BASE
from sqlalchemy.orm import Mapped, mapped_column
import datetime

class AQI(BASE):
    __tablename__ = "AQI"
    state_code : Mapped[str] = mapped_column(String(50))
    county_code : Mapped[str] = mapped_column(String(50))
    site_number : Mapped[str] = mapped_column(String(50))
    parameter_code : Mapped[str] = mapped_column(String(50))
    sample_duration : Mapped[str] = mapped_column(String(50))
    sample_duration_code : Mapped[str] = mapped_column(String(50))
    sample_frequency : Mapped[str] = mapped_column(String(50))
    state : Mapped[str] = mapped_column(String(50))
    county : Mapped[str] = mapped_column(String(50))
    date_gmt : Mapped[datetime.datetime] = mapped_column(String(50))
    time_gmt : Mapped[str] = mapped_column(String(50))

    __table_args__ = (
        PrimaryKeyConstraint("state_code", "county_code", "site_number", "parameter_code", date_gmt, time_gmt),
    )
    
    
class Cases(BASE):
    __tablename__ = "Cases"
    date = mapped_column(DATE)
    location = mapped_column(String(50))
    new_cases = mapped_column(String(50))
    new_deaths = mapped_column(String(50))
    
    __table_args__ = (
        PrimaryKeyConstraint("date", "location"),
    )

class Mortality(BASE):
    __tablename__ = "Mortality"
    date = mapped_column(DATE)
    country = mapped_column(String(50))
    cumulative_estimated_daily_excess_death = mapped_column(Float)
    cumulative_estimated_daily_excess_deaths_per_100k = mapped_column(Float)
    estimated_daily_excess_deaths = mapped_column(Float)
    estimated_daily_excess_deaths_per_100k = mapped_column(Float)
    
    __table_args__ = (
        PrimaryKeyConstraint("date", "country"),
    )

class Population(BASE):
    __tablename__ = "Population"
    country = mapped_column(String(50))
    population = mapped_column(Integer)
    
    __table_args__ = (
        PrimaryKeyConstraint("country"),
    )

class Vaccination(BASE):
    __tablename__ = "Vaccination"
    date = mapped_column(DATE)
    location = mapped_column(String(50))
    total_vaccinations = mapped_column(Integer)
    people_vaccinated = mapped_column(Integer)
    daily_vaccinations = mapped_column(Integer)
    daily_people_vaccinated = mapped_column(Integer)

    __table_args__ = (
        PrimaryKeyConstraint("date", "location"),
    )

class StringencyIndex(BASE):
    __tablename__ = "StringencyIndex"
    date = mapped_column(DATE)
    country = mapped_column(String(50))
    StringencyIndex_Avg = mapped_column(Float)
    
    __table_args__ = (
        PrimaryKeyConstraint("date", "country"),
    )
    
class Hospitalization(BASE):
    __tablename__ = "Hospitalization"
    date = mapped_column(DATE)
    country = mapped_column(String(50))
    daily_hospital_occupancy = mapped_column(Integer)
    daily_icu_occupancy = mapped_column(Integer)

    __table_args__ = (
        PrimaryKeyConstraint("date", "country"),
    )