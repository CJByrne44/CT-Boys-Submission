def initDatabase():
    from cassandra.cluster import Cluster
    from cassandra.auth import PlainTextAuthProvider
    cloud_config = {
        'secure_connect_bundle': 'C:\\Users\conne\\PycharmProjects\\kivyProject\\secure-connect-users.zip'
    }
    auth_provider = PlainTextAuthProvider('CTBoys', 'CTBoyspassword1')
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()
    session.execute("USE users")
    return session