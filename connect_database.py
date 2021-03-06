import sys
import csv
from database_functions import initDatabase

session = initDatabase()
session.execute("USE users")
with open('people.csv', 'r') as csvFile:
        reader = csv.DictReader(csvFile)
        for line in reader:
                nums = []
                idnum = session.execute("SELECT id FROM users")
                for row in idnum:
                        nums.append(row[0])
                if nums == []:
                        id = 1
                else:
                        id = max(nums) + 1
                stmt = session.prepare("""
                INSERT INTO users(id, first, last, university, major)
                VALUES(?, ?, ?, ?, ?)
                IF NOT EXISTS
                """)
                results = session.execute(stmt, [id, line['first'], line['last'], line['university'], line['major']])
                #session.execute('INSERT INTO users (id, first, last, university, major) VALUES (?, ?, ?, ?, ?);'(id, line['first'], line['last'], line['university'], line['major']))
