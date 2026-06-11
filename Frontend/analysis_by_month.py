import pandas as pd
import streamlit as st
import requests
from datetime import datetime

API_URL = "http://localhost:8000"

def analysis_month_tab():
    response = requests.get(f"{API_URL}/monthly_summary/")
    response=response.json()

    df = pd.DataFrame(response)

    df = df.rename(columns={
        "month_number": "Month Number",
        "month_name": "Month Name",
        "total": "Total"
    })
    df_sorted = df.sort_values(by='Month Number')
    df_sorted.set_index('Month Number', inplace=True)
    st.title("Expense breakdown by Month")
    st.bar_chart(data=df_sorted.set_index("Month Name")['Total'])

    # to reduce decimal precision
    df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)
    st.table(df_sorted)
