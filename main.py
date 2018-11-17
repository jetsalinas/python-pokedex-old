from interface import Interface
from files.database import Database

if __name__ == "__main__":

    # TODO: handle command line arguments
    database = Database()
    [print(row.name) for row in database.filter_by_type("poison")]
    interface = Interface(database)
    interface.start()