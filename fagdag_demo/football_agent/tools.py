import sqlite3
from pathlib import Path

import pandas as pd


def query_database(query: str) -> dict:
    """
    Query the database with the given query string and return the results as a Markdown-formatted table.

    The database is an SQLite3 database with information about Football results. The database has the following structure:
    - Table: results
      - Columns: id, date, home_team, away_team, home_score, away_score

    Example query: "SELECT home_team, away_team, home_score, away_score FROM results WHERE date == '2022-01-01';"

    Args:
        query (str): The SQL query to execute against the database.

    Returns:
        dict: status and result or error message.
    """
    database_path = Path(__file__).parent.parent.parent / "data" / "database.db"
    try:
        with sqlite3.connect(database_path) as conn:
            df = pd.read_sql_query(query, conn)
    except Exception as e:
        return {
            "status": "error",
            "result": f"An error occurred while querying the database: {str(e)}",
        }

    if df.empty:
        return {"status": "success", "result": "No results found."}

    return {"status": "success", "result": df.to_markdown(index=False)}


if __name__ == "__main__":
    # Example usage
    query = "SELECT home_team, away_team, home_score, away_score FROM results WHERE date == '2022-01-01';"
    result = query_database(query)
    print(result)
