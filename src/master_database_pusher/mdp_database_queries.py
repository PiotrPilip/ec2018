from configparser import ConfigParser
from cassandra.cluster import Cluster


cfg = ConfigParser()
cfg.read('../../main.conf')


def insert_data(columns,data,table):
    cluster = Cluster()
    session = cluster.connect('tutorial')

    query = "INSERT INTO {} (".format(table)
    for col in columns:
        query+=' {},'.format(col)
    query=query[:-1]
    query+=') VALUES ('
    for col in columns:
        query+=' %s,'.format(col)
    query=query[:-1]+')'
    print(query)



if __name__ == '__main__':
    insert_data(['lol','d'],['xd',1],'kwejk')