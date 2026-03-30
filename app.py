import pandas as pd
import streamlit as st
import logic

st.title("Faculty Grade Dashboard")
col1, col2, col3 = st.columns(3)
average, highest, lowest = logic.calculate_stats(dataframe)

col1.metric("Average", f"{average:.1f}")
col2.metric("Highest", highest)
col3.metric("Lowest", lowest)

st.table(dataframe)