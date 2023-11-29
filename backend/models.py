from db import db_obj
from sqlalchemy import (
    text,
    PrimaryKeyConstraint,
    String,
    Float,
    Integer,
    DATE,
    Index,
)

BASE = db_obj.BASE
from sqlalchemy.orm import Mapped, mapped_column
import datetime


class AQI(BASE):
    __tablename__ = "AQI"
    state_code: Mapped[str] = mapped_column(String(50))
    county_code: Mapped[str] = mapped_column(String(50))
    site_number: Mapped[str] = mapped_column(String(50))
    parameter_code: Mapped[str] = mapped_column(String(50))
    sample_duration: Mapped[str] = mapped_column(String(50))
    sample_duration_code: Mapped[str] = mapped_column(String(50))
    sample_frequency: Mapped[str] = mapped_column(String(50))
    state: Mapped[str] = mapped_column(String(50))
    county: Mapped[str] = mapped_column(String(50))
    date_gmt: Mapped[datetime.datetime] = mapped_column(String(50))
    time_gmt: Mapped[str] = mapped_column(String(50))

    __table_args__ = (
        PrimaryKeyConstraint(
            "state_code",
            "county_code",
            "site_number",
            "parameter_code",
            date_gmt,
            time_gmt,
        ),
    )


class Cases(BASE):
    __tablename__ = "Cases"
    date = mapped_column(DATE)
    location = mapped_column(String(50))
    new_cases = mapped_column(String(50))
    new_deaths = mapped_column(String(50))

    __table_args__ = (
        PrimaryKeyConstraint("date", "location"),
        Index('index_cases_location', 'location'),
        Index('index_new_cases', 'new_cases'),
        Index('index_new_deaths', 'new_deaths'),
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
        Index('index_mortality_country','country'),
        Index('index_cumulative_estimated_daily_excess_death', 'cumulative_estimated_daily_excess_death'),
        Index('index_cumulative_estimated_daily_excess_deaths_per_100k', 'cumulative_estimated_daily_excess_deaths_per_100k'),
        Index('index_estimated_daily_excess_deaths', 'estimated_daily_excess_deaths'),
        Index('index_estimated_daily_excess_deaths_per_100k', 'estimated_daily_excess_deaths_per_100k'),
    )



class Population(BASE):
    __tablename__ = "Population"
    country = mapped_column(String(50))
    population = mapped_column(Integer)

    __table_args__ = (
        PrimaryKeyConstraint("country"),
        Index('index_population', 'population')
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
        Index('index_vaccination_location', 'location'),
        Index('index_total_vaccinations', 'total_vaccinations'),
        Index('index_people_vaccinated', 'people_vaccinated'),
        Index('index_daily_vaccinations', 'daily_vaccinations'),
        Index('index_daily_people_vaccinated', 'daily_people_vaccinated'),
    )


class StringencyIndex(BASE):
    __tablename__ = "StringencyIndex"
    date = mapped_column(DATE)
    country = mapped_column(String(50))
    StringencyIndex_Avg = mapped_column(Float)

    __table_args__ = (
        PrimaryKeyConstraint("date", "country"),
        Index('index_StringencyIndex_country', 'country'),
        Index('index_StringencyIndex_Avg', 'StringencyIndex_Avg'),
    )


class Testing(BASE):
    __tablename__ = "Testing"
    date = mapped_column(DATE)
    country = mapped_column(String(50))
    new_tests_smoothed = mapped_column(Integer)

    __table_args__ = (
        PrimaryKeyConstraint("date", "country"),
        Index('index_testing_country','country'),
        Index('index_new_tests_smoothed', 'new_tests_smoothed'),
    )


class Hospitalization(BASE):
    __tablename__ = "Hospitalization"
    date = mapped_column(DATE)
    country = mapped_column(String(50))
    daily_hospital_occupancy = mapped_column(Integer)
    daily_icu_occupancy = mapped_column(Integer)

    __table_args__ = (
        PrimaryKeyConstraint("date", "country"),
        Index('index_hospitalization_country', 'country'),
        Index('index_daily_hospital_occupancy', 'daily_hospital_occupancy'),
        Index('index_daily_icu_occupancy', 'daily_icu_occupancy'),
    )


class Parameters(BASE):
    __tablename__ = "Parameters"
    country = mapped_column(String(50))
    gdp_per_capita = mapped_column(Float)
    cardiovasc_death_rate = mapped_column(Float)
    diabetes_prevalence = mapped_column(Float)
    hospital_beds_per_thousand = mapped_column(Float)

    __table_args__ = (
        PrimaryKeyConstraint("country"),
        Index('index_gdp_per_capita', 'gdp_per_capita'),
        Index('index_cardiovasc_death_rate', 'cardiovasc_death_rate'),
        Index('index_diabetes_prevalence', 'diabetes_prevalence'),
        Index('index_hospital_beds_per_thousand', 'hospital_beds_per_thousand'),
    )

class Emissions(BASE):
    __tablename__ = "Emissions"
    country = mapped_column(String(50))
    year = mapped_column(Integer)
    total_emissions = mapped_column(Float)
    co2_emission_coal = mapped_column(Float)
    co2_emission_oil = mapped_column(Float)
    co2_emission_gas = mapped_column(Float)
    co2_emission_cement = mapped_column(Float)
    co2_emission_flaring = mapped_column(Float)
    co2_emission_per_capita = mapped_column(Float)

    __table_args__ = (
        PrimaryKeyConstraint("country", "year"),
        Index('index_emissions_country', 'country'),
        Index('index_emissions_year', 'year'),
        Index('index_total_emissions', 'total_emissions'),
        Index('index_co2_emission_coal', 'co2_emission_coal'),
        Index('index_co2_emission_oil', 'co2_emission_oil'),
        Index('index_co2_emission_gas', 'co2_emission_gas'),
        Index('index_co2_emission_cement', 'co2_emission_cement'),
        Index('index_co2_emission_flaring', 'co2_emission_flaring'),
        Index('index_co2_emission_per_capita', 'co2_emission_per_capita'),
    )

    
class HDI(BASE):
    __tablename__ = "HDI"
    year = mapped_column(Integer)
    country = mapped_column(String(50))
    le = mapped_column(Float)
    eys = mapped_column(Float)
    mys = mapped_column(Float)
    gnipc = mapped_column(Float)

    __table_args__ = (
        PrimaryKeyConstraint("country", "year"),
        Index('index_hdi_country','country'),
        Index('index_hdi_year', 'year'),
        Index('index_le', 'le'),
        Index('index_eys', 'eys'),
        Index('index_mys', 'mys'),
        Index('index_gnipc', 'gnipc'),
    )

from sqlalchemy import Index

class Inequality(BASE):
    __tablename__ = "Inequality"
    year = mapped_column(Integer)
    country = mapped_column(String(50))
    abr = mapped_column(Float)
    mmr = mapped_column(Float)
    prf = mapped_column(Float)
    sef = mapped_column(Float)
    prm = mapped_column(Float)
    sem = mapped_column(Float)
    lfprf = mapped_column(Float)
    lfprm = mapped_column(Float)

    __table_args__ = (
        PrimaryKeyConstraint("country", "year"),
        Index('index_inequality_country','country'),
        Index('index_inequality_year', 'year'),
        Index('index_abr', 'abr'),
        Index('index_mmr', 'mmr'),
        Index('index_prf', 'prf'),
        Index('index_sef', 'sef'),
        Index('index_prm', 'prm'),
        Index('index_sem', 'sem'),
        Index('index_lfprf', 'lfprf'),
        Index('index_lfprm', 'lfprm'),
    )