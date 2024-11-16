class MultidbConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://db_user:12345@127.0.0.1:5432/default_database"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {
        'asia_database': 'postgresql://db_user:12345@127.0.0.1:5432/asia_database',
        'europe_database': 'postgresql://db_user:12345@127.0.0.1:5432/europe_database',
        'america_database': 'postgresql://db_user:12345@127.0.0.1:5432/america_database'
}