from configparser import ConfigParser
from cassandra.cluster import Cluster


cfg = ConfigParser()
cfg.read('../../main.conf')


def insert_data(columns,data,table):
    cluster = Cluster()
    session = cluster.connect(cfg["DATABASE"]['keyspace_md'])

    query = "INSERT INTO {} (".format(table)
    for col in columns:
        query+=' {},'.format(col)
    query=query[:-1]
    query+=') VALUES ('
    for col in columns:
        query+=' %s,'.format(col)
    query=query[:-1]+')'
    print(query)
    session.execute( query,data  )


def insert_twitter_dic(dictonary,keyword):
    columns = [ k for k in dictonary.keys() ]
    data = [dictonary[k] for k in dictonary.keys()]
    insert_data(columns,data,keyword)

