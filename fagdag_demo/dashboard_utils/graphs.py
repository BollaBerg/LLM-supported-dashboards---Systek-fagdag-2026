import plotly.express as px
import streamlit as st
from dataloader import run_query


def teams_by_win_rate():
    data = run_query(
        """
        WITH wins AS (
            SELECT
                CASE 
                    WHEN home_score > away_score THEN home_team 
                    WHEN away_score > home_score THEN away_team 
                    ELSE NULL 
                END AS winning_team
            FROM results
        ),
        total_wins AS (
            SELECT winning_team AS team, COUNT(*) AS wins
            FROM wins
            WHERE winning_team IS NOT NULL
            GROUP BY winning_team
        ),
        matches AS (
            SELECT home_team AS team, COUNT(*) AS total
            FROM results
            GROUP BY home_team
            UNION ALL
            SELECT away_team AS team, COUNT(*) AS total
            FROM results
            GROUP BY away_team
        ),
        total_matches AS (
            SELECT team, SUM(total) AS total
            FROM matches
            GROUP BY team
        )
        SELECT 
            m.team, 
            COALESCE(w.wins, 0) AS wins, 
            COALESCE(m.total, 0) AS total_matches,
            CASE 
                WHEN COALESCE(m.total, 0) > 0 THEN ROUND(COALESCE(w.wins, 0) * 100.0 / m.total, 2) 
                ELSE 0 
            END AS win_rate
        FROM total_matches m
        LEFT JOIN total_wins w ON m.team = w.team
        WHERE m.total > 10
        ORDER BY win_rate DESC
        LIMIT 10;
        """
    )

    fig = px.bar(data, x="team", y="win_rate", title="Top 10 Teams by Win Rate")

    st.plotly_chart(fig)


def teams_by_total_wins():
    data = run_query(
        """
        WITH wins AS (
            SELECT
                CASE 
                    WHEN home_score > away_score THEN home_team 
                    WHEN away_score > home_score THEN away_team 
                    ELSE NULL 
                END AS winning_team
            FROM results
        ),
        total_wins AS (
            SELECT winning_team AS team, COUNT(*) AS wins
            FROM wins
            WHERE winning_team IS NOT NULL
            GROUP BY winning_team
        )
        SELECT team, wins
        FROM total_wins
        ORDER BY wins DESC
        LIMIT 10;
        """
    )

    fig = px.bar(data, x="team", y="wins", title="Top 10 Teams by Total Wins")

    st.plotly_chart(fig)
