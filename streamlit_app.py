import streamlit as st
import soundfile as sf
import sounddevice as sd

def play_sound(sound_file):
    data, samplerate = sf.read(sound_file)
    sd.play(data, samplerate)
    sd.wait()

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
                play_sound("ocean_waves.wav")
            elif sound_choice == "Rainforest":
                play_sound("rainforest.wav")
            elif sound_choice == "Soft Piano":
                play_sound("soft_piano.wav")

    elif option == "Breathing Exercises":
        st.write("Practice deep breathing exercises to calm your mind and body.")
        st.write("Inhale deeply through your nose, hold your breath for a few seconds, then exhale slowly through your mouth.")
        if st.button("Start"):
            # TODO: Add code for breathing exercise timer
            st.write("Breathing exercise started.")

if __name__ == '__main__':
    main()
