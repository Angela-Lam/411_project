"""Defines all the functions related to the database"""
from app import db
import sqlalchemy
from datetime import date

def fetch_users() -> list:
    """Reads all user information from the User table

    Returns:
        A list of dictionaries
    """
    conn = db.connect()
    query_results = conn.execute("SELECT * FROM User;").fetchall()
    conn.close()
    users = []
    for result in query_results:
        user = {
            "id": result[0], 
            "username": result[1], 
            "password": result[2], 
            "join_date": result[3] 
        }
        users.append(user)
    return users

def fetch_fav() -> list:
    conn = db.connect()
    query_results = conn.execute("SELECT * FROM Favorites;").fetchall()
    conn.close()
    favs = []
    for result in query_results:
        fav = {
            "VideoId": result[0], 
            "UserId": result[1]
        }
        favs.append(fav)
    return favs

# NICK 
def fetch_history() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """

    conn = db.connect()
    query_results = conn.execute("Select * from Search;").fetchall()
    conn.close()
    history_list = []
    for result in query_results:
        item = {
            "SearchId": result[0],
            "Timestamp": result[1],
            "Querry": result[2]
        }
        history_list.append(item)

    return history_list

def fetch_homepage() -> dict:
    """
    Returns:
        A list of dictionaries
    """
    conn = db.connect()
    query_results = conn.execute(sqlalchemy.text("Select * from User;")).fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "user_id": result[0],
            "username": result[1],
            "password": result[2],
            "join_date": result[3]
        }
        todo_list.append(item)
    return todo_list

def get_usernames():
    conn = db.connect()
    usernames = conn.execute(sqlalchemy.text("Select Username from User;")).fetchall()
    conn.close()
    return usernames

def get_users():
    conn = db.connect()
    users = conn.execute(sqlalchemy.text("Select Username, Password from User;")).fetchall()
    conn.close()
    return users

def add_user(username, password):
    conn = db.connect()
    ids_raw = conn.execute(sqlalchemy.text("Select UserId from User;")).fetchall()
    ids = [i[0] for i in ids_raw]
    new_id = max(ids) + 1
    today = date.today()
    today_int = 10000*today.year + 100*today.month + today.day
    command = "INSERT INTO User VALUES(" + str(new_id) + ", '" + username + "', '" + password + "', " + str(today_int) + ");"
    print(command)
    conn.execute(sqlalchemy.text(command))
    conn.commit()
    conn.close()

def update_task_entry(task_id: int, text: str) -> None:
    """Updates task description based on given `task_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated description

    Returns:
        None
    """

    conn = db.connect()
    query = 'Update tasks set task = "{}" where id = {};'.format(text, task_id)
    conn.execute(query)
    conn.close()


def update_status_entry(task_id: int, text: str) -> None:
    """Updates task status based on given `task_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated status

    Returns:
        None
    """

    conn = db.connect()
    query = 'Update tasks set status = "{}" where id = {};'.format(text, task_id)
    conn.execute(query)
    conn.close()


def insert_new_task(text: str) ->  int:
    """Insert new task to todo table.

    Args:
        text (str): Task description

    Returns: The task ID for the inserted entry
    """

    conn = db.connect()
    query = 'Insert Into tasks (task, status) VALUES ("{}", "{}");'.format(
        text, "Todo")
    conn.execute(query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    conn.close()

    return task_id


def remove_task_by_id(task_id: int) -> None:
    """ remove entries based on task ID """
    conn = db.connect()
    query = 'Delete From tasks where id={};'.format(task_id)
    conn.execute(query)
    conn.close()
