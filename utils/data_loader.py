# utils/data_loader.py
# handles Excel and image loading
import streamlit as st
import pandas as pd


def load_data(excel_path="data/profiles.xlsx"):
    """Load Excel data and handle missing file gracefully."""
    try:
        return pd.read_excel(excel_path)
    except FileNotFoundError:
        st.error(f"❌ Excel file not found: {excel_path}")
        st.stop()
