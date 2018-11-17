from interface import Interface
from files.database import Database

if __name__ == "__main__":

    # TODO: handle command line arguments
    # TODO: Implement csv loading
    database = Database()

    interface = Interface()
    interface.start()