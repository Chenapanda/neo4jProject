from neo4j import GraphDatabase

import parcours_csv

# Class for creating nodes and relations in neo4j
class Application:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()

    def create_node(self,name_of_node):
        with self.driver.session() as session:
            node_id = session.write_transaction(create_node_tx,name_of_node)

    def create_node_project(self, list_name_of_node):
        with self.driver.session() as session:
            node_id = session.write_transaction(create_node_tx_project,list_name_of_node)

    def create_node_lead(self, list_name_of_lead):
        with self.driver.session() as session:
            node_id = session.write_transaction(create_node_tx_lead,list_name_of_lead)

    def create_relation(self,list_one,list_second):
        with self.driver.session() as session:
            node_id = session.write_transaction(create_relation_tx,list_one,list_second)

# Creates a relation
def create_relation_tx(tx, list_pro, list_lead):
    for i in range(0, len(list_pro), 1):
        nature = "WOWOWO"
        toto = "match (a:Project{name: $project_name }) match (b:Lead{name: $lead_name}) create( (a)-[r:%s]->(b))RETURN r" % nature
        tx.run(toto, project_name=list_pro[i],lead_name=list_lead[i])

# Creates a lead node
def create_node_tx_lead(tx,list_name_of_lead):
    for name_of_lead in list_name_of_lead:
        tx.run("CREATE (n:Lead { name: $name }) RETURN id(n) AS node_id", name=name_of_lead)

# Creates a node
def create_node_tx(tx, name_of_node):
    result = tx.run("CREATE (n:First_try { name: $name }) RETURN id(n) AS node_id", name=name_of_node)
    record = result.single()
    return record["node_id"]


def create_node_tx_project(tx,list_name_of_node):
    for name_of_node in list_name_of_node:
        tx.run("CREATE (n:Project { name: $name }) RETURN id(n) AS node_id", name=name_of_node)


def collect_infos_leads(file_name):
    a,b,c,d,e,f,g = parcours_csv.read_file(file_name)
    infos = [a,b,c,d,e,f,g]
    value = ["Project","Lead","Binome","Lead_contact","Binome_contact","Lead_tel","Binome_tel"]
    return infos,value

