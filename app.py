import pandas as pd
import streamlit as st

col1, col2, col3 = st.columns(3)

col1.metric("Average", "Placeholder")
col2.metric("Highest", "Placeholder")
col3.metric("Lowest", "Placeholder")

current_roster = pd.DataFrame(
    {
        "Student": ["Placeholder"],
        "Grade": ["Placeholder"],
    },
    index =["Placeholder"],
)
st.table(current_roster)