import streamlit as st
import pandas as pd
from contacts import contact
import base64


#
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1709990740078-05aa8ee5b9b7?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=387");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

[data-testid="stSidebar"] {
    background-color: rgba(255,255,255,0.15);
    backdrop-filter: blur(5px);
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)
col1, col2 =st.columns(2)

with col1:
    st.image("assets/face.jpg",width = 275)
    
with col2:
    st.title("Joshua D. Arco",anchor=False)
    st.write(
        "Currently a 3rd year student at Cebu Institute of Technology - University(CIT-U) taking up the program of Computer Science"
    )
    with st.popover("📧 Contact Me"):
        contact()



st.subheader("Programming languages learned")
data = [
    {"name": "C", "image": "assets/c.png"},
    {"name": "C++", "image": "assets/cpp.png"},
    {"name": "Java", "image": "assets/java.png"},
    {"name": "Javascript", "image": "assets/javascript.png"},
    {"name": "Kotlin", "image": "assets/kotlin.jpg"},
    {"name": "Python", "image": "assets/python.jpg"},
]

for row in data:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.text(row["name"])
    with col2:
        st.image(row["image"], width=100)
        

st.subheader("Projects")
projects = [
    {
        "file": "assets/gamego.png",
        "url": "https://github.com/jones21312321313213/GameGo",
        "title": "GAMEGO:",
        "desc": "Developed a mobile app for gamers to discover,organize, and save favorite games using Firebase and livbe game data from external APIs"
    },
    {
        "file": "assets/stictactics.png",
        "url": "https://github.com/jones21312321313213/demoGame4OOP",
        "title": "STICTACTICS:",
        "desc": "Collaboratively developed a 2-player fighting game using OOP concepts featuring unique characters, special abilities and many arenas."
    },
    {
        "file": "assets/converter.png",
        "url": "https://github.com/jones21312321313213/CS132-FINAL-PROJECT",
        "title": "Converter:",
        "desc": "A lightweight tool built to convert numbers between decimal binary,octal and hexadecimal formats efficiently."
    },
    {
        "file": "assets/assemblygrocery.png",
        "url": "https://github.com/jones21312321313213/CS243-FINAL-PROJECT",
        "title": "Grocery Item-list:",
        "desc": "Designed a terminal-based mini system in x86 Assembly(TASM)implementing basic CRUD operations,user login, and verification logic."
    }
]

cols_per_row = 2
for i in range(0, len(projects), cols_per_row):
    cols = st.columns(cols_per_row)
    for j, project in enumerate(projects[i:i+cols_per_row]):
        with open(project["file"], "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
        html_code = f'''
            <h4 style="text-align:center; margin-bottom:5px;">{project["title"]}</h4>
            <a href="{project["url"]}" target="_blank">
                <img src="data:image/png;base64,{b64}" width="500" style="border-radius:10px; margin-bottom:5px;">
            </a>
            <p style="text-align:center; font-size:12px; color:gray;">{project["desc"]}</p>
        '''
        cols[j].markdown(html_code, unsafe_allow_html=True)