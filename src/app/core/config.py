import os

def get_mariadb_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = 3306 if host == "localhost" else 3306
    password = os.environ.get("DB_PASSWORD", "1234")
    user, db_name = "root", "allocation"
    return f"mysql+pymysql://{password}@{host}:{port}/{db_name}"

def get_mongodb_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = 27017 if host == "localhost" else 27017
    password = os.environ.get("DB_PASSWORD", "1234")
    user, db_name = "root", "allocation"
    return f'mongodb://{user}:{password}@{host}:{port}/{db_name}'