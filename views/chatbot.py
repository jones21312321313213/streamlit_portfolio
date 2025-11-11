import streamlit as st
import openai

st.title("Chat with this bot about the developer")


# Initialize OpenAI client
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


dev_responses = {
    ("food", "favorite food", "food dev likes", "food dev prefers"): "Pizza",
    ("color", "favorite color", "color dev likes"): "Red",
    ("movie", "favorite movie", "movie dev likes"): "Avengers: Infinity War",
    ("name", "dev name"): "Joshua D. Arco",
    ("from", "born", "hometown"): "Cebu, Philippines",
    ("birthday", "date of birth", "birth date"): "July 15, 2004",  
    ("age", "how old", "dev age"): "21",
    ("school", "university", "college"): "Cebu Institute of Technology (CIT)",
    ("study", "major", "what dev studies"): "BS Computer Science (BSCS)",
    ("skills", "programming", "languages dev knows"): "Good in C++ and Java",
    ("projects", "dev projects"): "Worked on e-commerce platforms and games",
    ("hobby", "free time", "what dev likes to do"): "Coding, playing games, watching anime, reading manga",
    ("sport", "favorite sport"): "Basketball",
    ("game", "favorite game"): "Dota 2",
    ("describe", "personality", "how is dev"): "Kind",
    ("motivate", "motivation", "what motivates dev"): "Food",
    ("goal", "ambition", "dev goal"): "To be a software engineer",
    ("animal", "favorite animal"): "Lion",
    ("height", "dev height"): "5'7\"",
    ("weight", "dev weight"): "85 kg",
    ("anime", "favorite anime"): "One Punch Man (OPM)",
    ("manga", "favorite manga"): "Attack on Titan",
    ("manhwa", "favorite manhwa"): "Return of the Mount Hua Sect",
    ("nba", "favorite NBA player"): "LeBron James",
    ("football", "favorite football player"): "Lionel Messi",
    ("programming language", "favorite programming language"): "C++",
    ("playstation", "favorite playstation game"): "God of War series",
    ("steam", "favorite steam game"): "Dota 2",
    ("riot", "favorite riot game"): "League of Legends",
    ("music", "favorite music genre"): "I listen to K-pop, Pop, and Hip-hop",
    ("pop artist", "favorite pop artist"): "Bruno Mars",
    ("hiphop artist", "favorite hiphop artist"): "Kendrick Lamar",
    ("kpop artist", "favorite kpop artist"): "NewJeans",
    ("song", "favorite song"): "I Wanna Be a Billionaire",
    ("dessert", "favorite dessert"): "Ice cream",
    ("ice cream", "favorite ice cream flavor"): "Strawberry",
    ("chocolate", "favorite chocolate brand"): "Cadbury",
    ("siblings", "how many siblings"): "3 siblings",
    ("dota rank", "highest rank in dota"): "Legend"
}


# React to user input
if prompt := st.chat_input('Type a messages like "what is dev favorite color"'):
    
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})
    prompt_lower = prompt.lower()

    # Check if user asks about the developer
    response = None
    for keys, val in dev_responses.items():
        if any(key in prompt_lower for key in keys):
            response = val
            break

    # Fallback to GPT if no keyword matches
    if response is None:
        try:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages
            )
            response = completion.choices[0].message.content
        except Exception:
            response = "I can't answer things not about the developer right now because the API quota has been exceeded."

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
