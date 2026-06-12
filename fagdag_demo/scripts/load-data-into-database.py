import sqlite3

import pandas as pd

if __name__ == "__main__":
    conn = sqlite3.connect("data/database.db")
    cursor = conn.cursor()

    # Create table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY,
            date TEXT NOT NULL,
            home_team TEXT NOT NULL,
            away_team TEXT NOT NULL,
            home_score INTEGER NOT NULL,
            away_score INTEGER NOT NULL,
            tournament TEXT NOT NULL,
            city TEXT NOT NULL,
            country TEXT NOT NULL,
            neutral BOOLEAN NOT NULL
        )
        """
    )

    # Load data from CSV
    df = pd.read_csv("data/results.csv")
    df.dropna(inplace=True)
    df.to_sql("results", conn, if_exists="replace", index=False)
