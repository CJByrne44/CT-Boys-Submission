def initDatabase():
    from cassandra.cluster import Cluster
    from cassandra.auth import PlainTextAuthProvider
    cloud_config = {
        'secure_connect_bundle': 'secure-connect-users.zip'
    }
    auth_provider = PlainTextAuthProvider('CTBoys', 'CTBoyspassword1')
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()
    session.execute("USE users")
    return session

def getID(session):
    nums = []
    idnum = session.execute("SELECT id FROM users")
    for row in idnum:
        nums.append(row[0])
    if nums == []:
        id = 1
    else:
        id = max(nums) + 1
    return id