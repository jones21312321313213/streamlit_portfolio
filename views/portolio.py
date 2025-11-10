import streamlit as st
import pandas as pd
from contacts import contact
import base64

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



st.subheader("Learned Programming Languages")
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

with open("assets/pizza.png", "rb") as f:
    data = f.read()
    b64 = base64.b64encode(data).decode()

st.markdown(
    f'<a href="https://www.youtube.com" target="_blank"><img src="data:image/png;base64,{b64}" width="200"></a>',
    unsafe_allow_html=True
)