# app.py
# handles layout and flow
import streamlit as st
from utils.data_loader import load_data
from utils.render import render_profile_card


def main():
    st.set_page_config(page_title="AI Tools Dashboard", layout="wide")
    st.title("🔍 AI Tools by Team Members")

    with open("styles/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    df = load_data()

    search_term = st.text_input("🔎 Search by name, email, tool, or role:", "").strip().lower()

    if search_term:
        df = df[df.apply(
            lambda row: search_term in str(row['Name']).lower()
                     or search_term in str(row['Email']).lower()
                     or search_term in str(row['AI Tools Used']).lower()
                     or search_term in str(row['Title']).lower(),
            axis=1
        )]
        if df.empty:
            st.warning("🙁 No matching results found.")
            st.stop()

    for _, row in df.iterrows():
        render_profile_card(row, search_term)


if __name__ == "__main__":
    main()
