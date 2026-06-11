import streamlit as st
from analysis_by_category import analysis_category_tab
from add_update import add_update_tab
from analysis_by_month import analysis_month_tab


API_URL = "http://localhost:8000"

st.title("Expense Management System")


tab1, tab2, tab3 = st.tabs(["Add/Update", "Analysis by Category", "Analysis by Month"])

with tab1:
    add_update_tab()
with tab2:
    analysis_category_tab()
with tab3:
    analysis_month_tab()





