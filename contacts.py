import streamlit as st
import re
import requests


WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTY0MDYzMDA0MzE1MjY0NTUzNDUxMzQi_pc"


def is_valid_email(email):
    #Basic regex pattern for email verification
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern,email) is not None

def contact():
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    if st.button("Submit"):
        if not WEBHOOK_URL:
            st.error("Email servie is not set up.Please try again later.")
            st.stop()
        
        if not name:
            st.error("Please provide your name.")
            st.stop()
            
        if not email:
            st.error("Please provide your email address.")
            st.stop()
            
        if not is_valid_email(email):
            st.error("Please provide a valid email address.")
            st.stop()
            
        if not message:
            st.error("Please provide a message.")
            st.stop()
            
        
        #Prepare the data payload and send it to the specified webhook URL
        data = {"email":email, "name":name, "message":message}
        response = requests.post(WEBHOOK_URL,json = data)
        
        if response.status_code == 200:
            st.success("Your message has been sent successfully! ")
        else:
            st.error("There was an erorr sending your message.")
             