import streamlit as st
import pandas as pd
import numpy as np


#st.set_page_config(layout="wide")
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1729179664855-9c068fec328d?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=870");
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

if "map_data" not in st.session_state:
    st.session_state['map_data'] = pd.DataFrame({
        'lat': [18.2038, 16.4023, 14.5995, 12.8797, 10.3157, 9.3076, 7.1907, 8.4542, 6.9214, 13.4125, 11.2408],
        'lon': [120.5951, 120.5960, 120.9842, 118.7386, 123.8854, 125.2551, 122.0740, 123.7000, 125.0945, 121.9245, 125.0483]
    })
    
one, two, three = st.columns(3)
with two:
    st.image("assets/face.jpg", width='stretch')
    
    

col1, col2, col3 = st.columns([2, 4, 2]) 
color_red = "red"
color_blue = "blue"
color_pizza = "#FF6347"
color_yellow = "yellow"
color_brown = "brown"
color_green = "green"
color_lightblue = "#ADD8E6"
color_gold = "#FFD700"
with col1:
    st.map(st.session_state['map_data'])
    st.caption("This is where i live")
    
with col2:
    st.markdown(
        f"""
        My name is Joshua D. Arco.I was born Cebu City, Philippines.<br>

        My childhood was all about playing with my siblings and friends across the street,<br>
        and watching TV shows like Courage the Cowardly Dog, Ben 10, SpongeBob, and many other iconic shows.<br><br>

        From an early age, I was exposed to the world of the internet and found it fascinating<br>
        that a computer can do so many things. I always remember playing Y8/Flash games like<br>
        <span style='color:{color_pizza}'>Papa’s Pizzeria series</span>,  <span style='color:{color_red}'> Fireboy</span> and  <span style='color:{color_blue}'>Watergirl</span>, <span style='color:{color_yellow}'>Bad</span> <span style='color:{color_brown}'>Ice-Cream</span>, and <span style='color:{color_green}'>Ben10: Savage Pursuit</span> on my computer
        and having fun with it.<br><br>

        But as I grew older, I started playing online games like  <span style='color:{color_yellow}'>CSGO</span>,  <span style='color:{color_red}'>DOTA2</span>,  <span style='color:{color_lightblue}'>Fortnite</span>,  <span style='color:{color_gold}'> LOL</span>, and  <span style='color:{color_red}'> Valorant</span>.<br>
        While playing these games, I often thought about how they were made — and with this curiosity,<br>
        it led me to take on the Computer Science program.  
        """,
        unsafe_allow_html=True
    )
    
with col3:

    st.image("assets/courage.png")
    st.caption("GOAT cartoon network show IMO")
    
    st.image("assets/pizza.png")
    st.caption("Best flash game in y8 no debate frfr")
    
    st.image("assets/dota2.png")
    st.caption("hardest game i ever played since i have to play with 4 animals")