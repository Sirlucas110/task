import sqlite3 as SQL

def getUsers() -> list:

    db = SQL.connect("db/users.db")

    sql_query = "SELECT * from users"

    usuarios = db.execute(sql_query).fetchall()

    db.close()
    return usuarios


def getId(user_id: int) -> tuple:

    db = SQL.connect("db/users.db")

    sql_query  = "SELECT * FROM users WHERE id=?"

    userID = db.execute(sql_query, (user_id,)).fetchone()

    db.close()
    return userID