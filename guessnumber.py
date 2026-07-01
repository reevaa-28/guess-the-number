import streamlit as st
import random
import base64

st.set_page_config(
    page_title="Guess The Number",     
    page_icon="🎲",
    layout="centered"
)

def set_bg(image_file):     
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image:
            linear-gradient(
                rgba(0,0,0,0.4),
                rgba(0,0,0,0.4)
            ),
            url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        .title {{
            text-align: center;
            color: white;
            font-size: 55px;
            font-weight: bold;
        }}

        .subtitle {{
            text-align: center;
            color:grey;
            font-size: 20px;
            margin-bottom: 20px;
        }}

        .game-box {{
            background: rgba(255,255,255,0.15);
            backdrop-filter: blur(10px);
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0px 5px 20px rgba(0,0,0,0.4);
        }}

        .score {{
            text-align: center;
            color: white;
            font-size: 25px;
            font-weight: bold;
            margin-bottom: 15px;
        }}

        .stButton button {{
            width: 100%;
            height: 50px;
            font-size: 18px;
            font-weight: bold;
            border-radius: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg("image.jpg")

if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 20)

if "score" not in st.session_state:
    st.session_state.score = 0

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

st.markdown(
    "<p class='title'>🎲 Guess The Number</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Guess a number between 1 and 20</p>",
    unsafe_allow_html=True
)

st.markdown(
    f"<p class='score'>🏆 Score: {st.session_state.score}</p>",
    unsafe_allow_html=True
)

with st.container():

    st.markdown("<div class='game-box'>", unsafe_allow_html=True)

    guess = st.number_input(
        "Enter Your Guess",
        min_value=1,
        max_value=20,
        step=1
    )

    col1, col2 = st.columns(2)      

    with col1:
        check = st.button("✅ Check Guess")

    with col2:
        new_game = st.button("🔄 New Game")

    st.markdown("</div>", unsafe_allow_html=True)

if check:
    st.session_state.attempts += 1

    if guess < st.session_state.number:
        st.warning("📉 Too Low! Try Again.")

    elif guess > st.session_state.number:
        st.warning("📈 Too High! Try Again.")

    else:
        st.success("🎉 Congratulations! You guessed correctly!")
        st.balloons()

        st.session_state.score += 1
        st.session_state.number = random.randint(1, 20)
        st.session_state.attempts = 0

st.info(f"🎯 Attempts: {st.session_state.attempts}")

if new_game:
    st.session_state.number = random.randint(1, 20)
    st.session_state.attempts = 0
    st.info("🎲 New Game Started!")