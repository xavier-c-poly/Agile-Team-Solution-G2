import streamlit as st
import pandas as pd


dataframe = pd.DataFrame({
    "Names": [],
    "Grades": []
})


def sidebar():
    st.sidebar.header("Entry Form")
    name = st.sidebar.text_input("Student Name")
    grade = st.sidebar.number_input("Score", min_value= 0, max_value= 100)
    
    if st.sidebar.button("Add Student") and name and grade:
        dataframe.loc[len(dataframe)] = (name, grade)


if __name__ == "__main__":
    sidebar()