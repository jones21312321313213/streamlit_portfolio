import streamlit as st


# -- Page Setup --
about_page = st.Page(
    page="views/about_me.py",
    title = "About Me",
    icon = ":material/account_circle:",
    default = True
)

portfolio_page = st.Page(
    page="views/portolio.py",
    title = "Profile",
    icon = ":material/business_center:",
   
)

chatbot_page = st.Page(
    page="views/chatbot.py",
    title = "Chatbot",
    icon = ":material/robot_2:",   
)

# ---- NAVIGATION SETUP [without sections] ---
#pg = st.navigation(pages=[about_page,portfolio_page,chatbot_page])

# -- NAVIGATION SETUP[with sections]--
pg = st.navigation(
    {
        "Autobiography":[about_page],
        "Portfolio":[portfolio_page],
        "Chatbot":[chatbot_page]
    }
)

#Shared on all pages
st.logo("assets/toilet.jpg")
st.sidebar.text("Made by Joshua D. Arco")

# --- Run navigation --
pg.run()