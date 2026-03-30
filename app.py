import streamlit as st

# Use st.bar_chart to display the distribution data
# provided by the logic module

st.markdown("# Faculty Grade Dashboard")

average = 3
lowest = 1
highest = 5

st.markdown(f"#### Average: {average}")
st.markdown(f"#### Highest: {highest}")
st.markdown(f"#### Lowest: {lowest}")

st.markdown("## Grade Distribution")
st.bar_chart({
    'A': 2,
    'B': 0,
    'C': 1,
    'D': 1,
    'F': 1
})

st.markdown("## Current Roster")
st.dataframe("Jordan's dataframe goes here")
