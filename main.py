
from neo4j import GraphDatabase
from neo4j import exceptions
import parcours_csv
from Application import Application, collect_infos_leads

if __name__ == "__main__":
    infos,val = collect_infos_leads("liste_leads.csv")
    test = Application("bolt://localhost:7687", "neo4j", "1234")
    test.create_node_project(infos[0])
    test.create_node_lead(infos[1])
    test.create_relation(infos[0],infos[1])
    test.close()