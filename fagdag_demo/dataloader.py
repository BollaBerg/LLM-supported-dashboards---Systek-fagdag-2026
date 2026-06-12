import sqlite3

import pandas as pd


def run_query(query: str):
    with sqlite3.connect("data/database.db") as conn:
        df = pd.read_sql_query(query, conn)

    return df
