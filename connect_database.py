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
        for line in reader:
                nums = []
                idnum = session.execute("SELECT id FROM users")
                for row in idnum:
                        nums.append(row[0])
                id = max(nums) + 1
                stmt = session.prepare("""
                INSERT INTO users(id, first, last, university, major)
                VALUES(?, ?, ?, ?, ?)
                IF NOT EXISTS
                """)
                results = session.execute(stmt, [id, line['first'], line['last'], line['university'], line['major']])
                #session.execute('INSERT INTO users (id, first, last, university, major) VALUES (?, ?, ?, ?, ?);'(id, line['first'], line['last'], line['university'], line['major']))


rows = session.execute("SELECT * FROM users")
for row in rows:
        for item in row:
                print(item)