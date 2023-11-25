from typing import Any
from dotenv import load_dotenv
from sqlalchemy import create_engine, text, inspect
import os
from sqlalchemy.orm import sessionmaker, DeclarativeBase


class DbUtils:
    def __init__(self) -> None:
        load_dotenv()
        self.DB_USER = os.getenv("DB_USER")
        self.DB_PASS = os.getenv("DB_PASSWORD")
        self.DB_HOST = os.getenv("DB_HOST")
        self.DB_PORT = os.getenv("DB_PORT")
        self.DB_SDN = os.getenv("DB_SDN")
        self.DB_URL = f"oracle+oracledb://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_SDN}"
        self.engine = create_engine(self.DB_URL)
    
    class BASE(DeclarativeBase):
            pass


    def get_session(self):
        Session = sessionmaker(bind=self.engine)
        return Session()
    
    def execute_raw(self, query: str):
        session = self.get_session()
        result = session.execute(text(query))
        session.close()
        return result
    
    def check_table_exists(self, table_name: str) -> bool:
        inspector = inspect(self.engine)
        flag =  inspector.has_table(table_name)
        return flag

    def create_all(self, table_name: str):
        self.BASE.metadata.create_all(self.engine, tables=[table_name])

    def create_table(self, table_name: str):
        if not self.check_table_exists(table_name):
            # self.create_all(Cases.__table__)
            if table_name == "AQI":
                from models import AQI
                self.create_all(AQI.__table__)
            elif table_name == "Cases":
                from models import Cases
                self.create_all(Cases.__table__)
            elif table_name == "Mortality":
                from models import Mortality
                self.create_all(Mortality.__table__)
            elif table_name == "Population":
                from models import Population
                self.create_all(Population.__table__)
            elif table_name == "Vaccination":
                from models import Vaccination
                self.create_all(Vaccination.__table__)
            elif table_name == "StringencyIndex":
                from models import StringencyIndex
                self.create_all(StringencyIndex.__table__)
            elif table_name == "Testing":
                from models import Testing
                self.create_all(Testing.__table__)
            elif table_name == 'Hospitalization':
                from models import Hospitalization
                self.create_all(Hospitalization.__table__)
            elif table_name == 'Parameters':
                from models import Parameters
                self.create_all(Parameters.__table__)
            elif table_name == 'Emissions':
                from models import Emissions
                self.create_all(Emissions.__table__)
        else:
            print(f"Table {table_name} already exists")
    
    def drop_table(self, table_name: str):
        if self.check_table_exists(table_name):
            self.BASE.metadata.drop_all(self.engine, tables=[table_name])
        else:
            print(f"Table {table_name} does not exist")
    
    def grant_access(self, table_name: str, user_name: str):
        if self.check_table_exists(table_name):
            query = f'GRANT SELECT,INSERT,UPDATE,DELETE ON "{table_name}" TO "{user_name}"'
            self.execute_raw(query)
        else:
            raise Exception(f"Table {table_name} does not exist")
         
    
db_obj = DbUtils()