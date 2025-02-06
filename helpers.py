# Standard library imports
import os
from functools import wraps

# Third-party libraries
from dotenv import load_dotenv
from flask import redirect, session
import psycopg2
from psycopg2.extras import RealDictCursor


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def get_db():
    """
    Establishes a connection to the PostgreSQL database using credentials 
    from the app's configuration.

    Returns:
        psycopg2.connection: A connection object to the PostgreSQL database.
    """
    load_dotenv()

    return psycopg2.connect(
        host=os.getenv("DBHOST"),
        dbname=os.getenv("DBNAME"),
        user=os.getenv("DBUSER"),
        password=os.getenv("DBPASSWORD")
    )


def db_execute(query, params=None, return_value=False):
    """
    Executes a given SQL query on the PostgreSQL database.

    Args:
        query (str): The SQL query to execute.
        params (tuple, optional): The parameters to be used in the query, default is None.
        return_value (bool, optional): If True, the function will return the results of 
                                      the query. Default is False.

    Returns:
        list: A list of dictionary results if return_value is True, otherwise None.
    
    Raises:
        Exception: If the query fails, the exception will be raised after a rollback.
    """
    db = get_db()
    cursor_factory = RealDictCursor if return_value else None
    cursor = db.cursor(cursor_factory=cursor_factory)
    
    try:
        cursor.execute(query, params)
        if return_value:
            results = cursor.fetchall()
            return results
        else:
            db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        cursor.close()
        db.close()
