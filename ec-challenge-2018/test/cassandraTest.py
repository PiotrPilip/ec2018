from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect('tutorial')
rows = session.execute('SELECT * FROM dupa')
for r in rows:
    print(r)


number = 2
text = 'Hi'
rows = session.execute( 'INSERT INTO dupa (id_dupa,name) VALUES (%s,%s)',(number,text,)  )
