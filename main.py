from interface import Interface
from files.database import Database

if __name__ == "__main__":

    # TODO: handle command line arguments
    database = Database()
    interface = Interface(database)
    interface.start()