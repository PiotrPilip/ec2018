from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect('tutorial')
rows = session.execute('SELECT * FROM dupa')
for r in rows:
    print(r)