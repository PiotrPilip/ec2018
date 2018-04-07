from configparser import ConfigParser
from cassandra.cluster import Cluster
import csv,re

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

def select_since(since,keyword,output):
    cluster = Cluster()
    session = cluster.connect(cfg["DATABASE"]['keyspace_md'])
    query = 'SELECT * FROM {} WHERE createtime > {} ALLOW FILTERING'.format(keyword,since)
    rows=session.execute(query)
    with open(output,'w') as csvfile:
        writer = csv.writer(csvfile)
        for row in rows:
            new_row = [ re.sub(r'[^a-zA-Z0-9_ ]+', '', str(k)) for k in row]
            writer.writerow(new_row)

