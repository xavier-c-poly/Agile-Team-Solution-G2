import streamlit as st
import pandas as pd
import logic

if "Roster" not in st.session_state:
    st.session_state["Roster"] = pd.DataFrame({
        "Names": [],
        "Grades": []
    })


st.title("Faculty Grade Dashboard")
col1, col2, col3 = st.columns(3)
average, highest, lowest = logic.calculate_stats(st.session_state["Roster"])

col1.metric("Average", f"{average:.1f}")
col2.metric("Highest", highest)
col3.metric("Lowest", lowest)


def sidebar():
    st.sidebar.header("Entry Form")
    name = st.sidebar.text_input("Student Name")
    grade = st.sidebar.number_input("Score", min_value= 0, max_value= 100)
    
    if st.sidebar.button("Add Student") and name and grade:
        st.session_state["Roster"].loc[len(st.session_state["Roster"])] = (name, grade)


if __name__ == "__main__":
    sidebar()
    st.markdown("## Grade Distribution")
    st.bar_chart(logic.get_grade_distribution(st.session_state["Roster"]))
    print(st.session_state["Roster"])