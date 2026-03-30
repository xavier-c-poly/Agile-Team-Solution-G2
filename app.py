import streamlit as st
import pandas as pd
import logic

if "Roster" not in st.session_state:
    st.session_state["Roster"] = pd.DataFrame({
        "Names": [],
        "Grades": []
    })


def sidebar():
    st.sidebar.header("Entry Form")
    name = st.sidebar.text_input("Student Name")
    grade = st.sidebar.number_input("Score", min_value= 0, max_value= 100)
    
    if st.sidebar.button("Add Student") and name and grade:
        st.session_state["Roster"].loc[len(st.session_state["Roster"])] = (name, grade)


if __name__ == "__main__":
    sidebar()
    st.markdown("## Grade Distribution")
    st.bar_chart(logic.get_grade_distribution(dataframe))
    print(dataframe)