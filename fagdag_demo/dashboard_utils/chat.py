import streamlit as st
from football_agent.runner import create_session, run_async


@st.fragment
def chat():
    if "session_id" not in st.session_state:
        st.session_state["session_id"] = create_session().id

    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    with st.container():
        if (
            st.session_state["chat_history"]
            and st.session_state["chat_history"][-1]["name"] == "user"
        ):
            content = st.write_stream(
                run_async(
                    session_id=st.session_state["session_id"],
                    new_message=st.session_state["chat_history"][-1]["message"],
                )
            )
            content_str = content if isinstance(content, str) else "".join(content)
            st.session_state["chat_history"].append(
                {"name": "assistant", "message": content_str}
            )

        st.subheader("Chat with the WC-preparation Bot")

        for message in st.session_state["chat_history"]:
            with st.chat_message(message["name"]):
                st.markdown(message["message"])

        if prompt := st.chat_input("Ask the bot about WC-preparation!"):
            st.session_state["chat_history"].append({"name": "user", "message": prompt})
            st.rerun(scope="fragment")
