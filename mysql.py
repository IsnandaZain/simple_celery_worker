import os
import MySQLdb


def connect():
    db_user = os.environ.get("DB_USER")
    db_name = os.environ.get("DB_NAME")
    db_host = os.environ.get("DB_HOST")
    db_pass = os.environ.get("DB_PASS")
    db = MySQLdb.connect(
        host=db_host,
        user=db_user,
        passwd=db_pass,
        db=db_name,
        charset="utf8",
        use_unicode=True
    )

    cursor = db.cursor()
    return db, cursor