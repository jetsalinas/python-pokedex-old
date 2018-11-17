import csv
import pandas as pd

class Database():

    def __init__(self, database="resources/data_test.csv"):
        self.database_address = database
        self.load()

    def load(self):
        self.database = pd.read_csv(self.database_address)