import streamlit as st
from playsound import playsound
import time

def play_sound(sound_file):
    playsound(sound_file)

def breathing_exercise(duration):
    st.write("Practice deep breathing exercises to calm your mind and body.")
    st.write("Inhale deeply through your nose, hold your breath for a few seconds, then exhale slowly through your mouth.")
    st.write(f"Duration: {duration} seconds")
    time.sleep(duration)
    st.write("Breathing exercise completed.")

def main():
    st.title("Meditation App")
    st.write("Welcome to the Meditation App!")
    st.write("Choose from the following options to relax and reduce stress:")

    option = st.selectbox(
        "Select an option",
        ("Guided Meditation", "Calming Sounds", "Breathing Exercises")
    )

    if option == "Guided Meditation":
        st.write("Sit comfortably, close your eyes, and listen to the guided meditation.")
        st.write("Press the Play button to start the meditation.")
        if st.button("Play"):
            # TODO: Add code to play guided meditation audio file
            st.write("Meditation is playing.")

    elif option == "Calming Sounds":
        st.write("Choose a calming sound to relax and unwind.")
        sound_choice = st.selectbox(
            "Select a sound",
            ("Ocean Waves", "Rainforest", "Soft Piano")
        )
        if st.button("Play"):
            if sound_choice == "Ocean Waves":
                play_sound("ocean_waves.mp3")
            elif sound_choice == "Rainforest":
                play_sound("rainforest.mp3")
            elif sound_choice == "Soft Piano":
                play_sound("soft_piano.mp3")

    elif option == "Breathing Exercises":
        duration = st.slider("Select the duration (in seconds)", 1, 10)
        if st.button("Start"):
            breathing_exercise(duration)

if __name__ == '__main__':
    main()
