import main
import parcours_csv

# Verify that the connection works, prints an error otherwise
def test_co():
    try:
        test = main.appli("bolt://localhost:7687", "neo4j", "1234")
        test.create_node("toto")
        test.close()
    except:
        print("Error on connection")

# Verify that the file is open, prints an error otherwise
def test_open_file(file_name):
    try:
        parcours_csv.read_file(file_name)
    except:
        print("error on openning or reading the file")


def tests():
    test_co()
    test_open_file()