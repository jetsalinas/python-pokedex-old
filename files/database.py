import csv
import pandas as pd

class Database():

    def __init__(self, database="resources/data_test.csv"):
        self.database_address = database
        self.load()

    def load(self):
        self.database = pd.read_csv(self.database_address)
        self.database_query = DatabaseQuery(self.database)

    def __iter__(self):
        return self.database_query.__iter__()

    def __getitem__(self, key):
        return self.database_query[key]

    def __setitem__(self, key, value):
        self.database_query[key] = value

    def get_by_name(self, name):
        query = self.database.loc[self.database.name == name]
        return DatabaseQuery(self.database.loc[self.database.name == name]) if not query.empty else None

    def get_by_index(self, key):
        return self.database_query[key]

    def get_indices_header(self):
        return [x for x in range(len(self.database_query))]

    def get_names_header(self):
        return [row.name for row in self.database_query]

class DatabaseQuery():
    
    def __init__(self, dataframe):
        self.query = []
        for index, row in dataframe.iterrows():
            data = []
            for col in row:
                data.append(col)
            self.query.append(DataRow(data))

    def __getitem__(self, key):
        return self.query[key]

    def __setitem__(self, key, value):
        self.query[key] = value

    def __iter__(self):
        return iter(self.query)

    def __len__(self):
        return len(self.query)

class DataRow():
    
    def __init__(self, serial):
        self.index = serial[0]
        self.abilities = serial[1]
        self.against_bug = serial[2]
        self.against_dark = serial[3]
        self.against_dragon = serial[4]
        self.against_electric = serial[5]
        self.against_fairy = serial[6]
        self.against_fight = serial[7]
        self.gainst_fire = serial[8]
        self.against_flying = serial[9]
        self.against_ghost = serial[10]
        self.against_grass = serial[11]
        self.against_ground = serial[12]
        self.against_ice = serial[13]
        self.against_normal = serial[14]
        self.against_poison = serial[15]
        self.against_psychic = serial[16]
        self.against_rock = serial[17]
        self.against_steel = serial[18]
        self.against_water = serial[19]
        self.attack = serial[20]
        self.base_egg_steps = serial[21]
        self.base_happiness = serial[22]
        self.base_total = serial[23]
        self.capture_rate = serial[24]
        self.classfication = serial[25]
        self.defense = serial[26]
        self.experience_growth = serial[27]
        self.height_m = serial[28]
        self.hp = serial[29]
        self.japanese_name = serial[30]
        self.name = serial[31]
        self.percentage_male = serial[32]
        self.pokedex_number = serial[33]
        self.sp_attack = serial[34]
        self.sp_defense = serial[35]
        self.speed = serial[36]
        self.type1 = serial[37]
        self.type2 = serial[38]
        self.weight_kg = serial[39]
        self.generation = serial[40]
        self.is_legendary = serial[41]