# from fuzzywuzzy import process
import streamlit as st
from rapidfuzz import process
## Question Bank
from questions.aiml import aiml_questions
from questions.flask import flask_questions
from questions.react import react_questions
from questions.app_development import appdev_questions
from questions.operating_systems import os_questions
from questions.dbms import dbms_questions
from questions.computer_networking import cn_questions
from questions.oops import oops_questions
from questions.coa import coa_questions
from questions.system_design import system_design_questions

final_questions = {}
topics_handled = {
    "Artificial Intelligence and Machine Learning" : aiml_questions,
    "App Development": appdev_questions,
    "Flask" : flask_questions,
    "React" : react_questions,
    "Operating System" : os_questions,
    "Computer Organization and Architecture" : coa_questions,
    "Database Management Systems" : dbms_questions,
    "Computer Networking" : cn_questions,
    "Object Oriented Programming Systems" : oops_questions,
    "System Design" : system_design_questions
}

if "question_history" not in st.session_state:
    st.session_state.question_history = {}



def prepare_final_question_set():
    global final_questions
    final_questions.update(aiml_questions)
    final_questions.update(flask_questions)
    final_questions.update(react_questions)
    final_questions.update(appdev_questions)
    final_questions.update(appdev_questions)
    final_questions.update(os_questions)
    final_questions.update(dbms_questions)
    final_questions.update(cn_questions)
    final_questions.update(oops_questions)
    final_questions.update(coa_questions)
    final_questions.update(system_design_questions)

def get_answer(question, topic):
    topic_array = topics_handled[topic]
    question = question.lower()
    question, score, _ = process.extractOne(question, topic_array.keys()) # _ is index of match in the list
    if score > 60:
        return topic_array[question]
    else:
        return "Sorry, I don't know that one yet."
    
prepare_final_question_set()

st.title("Welcome to ConverseGPT")

st.sidebar.title("Topics Handled:")
st.sidebar.write("1. Artificial Intelligence and Machine Learning")
st.sidebar.write("2. App Development")
st.sidebar.write("3. Flask")
st.sidebar.write("4. React")
st.sidebar.write("5. Operating System")
st.sidebar.write("6. Computer Organization and Architecture")
st.sidebar.write("7. Database Management Systems")
st.sidebar.write("8. Computer Networking")
st.sidebar.write("9. Object Oriented Programming Systems")
st.sidebar.write("10. System Design")

st.sidebar.title("Topics Handled:")

topic = st.selectbox(
    "Choose a topic:",
    [
        "Artificial Intelligence and Machine Learning",
        "App Development",
        "Flask",
        "React",
        "Operating System",
        "Computer Organization and Architecture",
        "Database Management Systems",
        "Computer Networking",
        "Object Oriented Programming Systems",
        "System Design"
    ]
)

question = st.text_input("You:", "")
if st.button("Ask"):
    answer = get_answer(question, topic)
    dicti = { f"You: {question}" : f"Bot: {answer}" }
    st.session_state.question_history.update(dicti)
    for key, value in st.session_state.question_history.items():
        st.markdown(
            f"<div style='background-color: #ffcccc; padding:10px; border-radius:10px; margin:5px 0; color: black'>{key}</div>",
            unsafe_allow_html=True
        )
        # Bot message (green background)
        st.markdown(
            f"<div style='background-color:#ccffcc; padding:10px; border-radius:10px; margin:5px 0; color: black'>{value}</div>",
            unsafe_allow_html=True
        )