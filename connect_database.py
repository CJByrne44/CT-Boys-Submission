from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

import sys
import csv

cloud_config= {
        'secure_connect_bundle': 'C:\\Users\conne\\PycharmProjects\\kivyProject\\secure-connect-users.zip'
}
auth_provider = PlainTextAuthProvider('CTBoys', 'CTBoyspassword1')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

session.execute("USE users")

with open('people.csv', 'r') as csvFile:
        reader = csv.DictReader(csvFile)
        test = session.execute("SELECT id FROM users")
        print(test)
        for line in reader:
                # session.execute("INSERT INTO users (id, first, last, university, major) VALUES(?, ?, ?, ?, ?)",
                #            (line['first'], line['last'], line['university'],
                #             line['major']))


rows = session.execute("SELECT * FROM users")
for row in rows:
        print(row)