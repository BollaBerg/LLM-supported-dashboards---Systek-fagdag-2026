import streamlit as st
from dashboard_utils.chat import chat
from dashboard_utils.graphs import teams_by_total_wins, teams_by_win_rate


def main():
    st.title("WC-preparation Dashboard")

    [col1, col2] = st.columns(2)
    with col1:
        teams_by_win_rate()
    with col2:
        teams_by_total_wins()

    chat()


if __name__ == "__main__":
    main()
