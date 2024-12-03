import streamlit as st
import os

def main():
    st.set_page_config(page_title="Music Player", page_icon="empty" , layout="wide", initial_sidebar_state="collapsed")
    st.title("🎵 Music Player")
    st.write("Upload your own music or play preloaded tracks!")

    # Sidebar for navigation
    st.sidebar.header("Options")
    option = st.sidebar.radio("Choose an option", ("Preloaded Songs", "Upload Your Song"))

    # Handle Preloaded Songs
    if option == "Preloaded Songs":
        st.subheader("Preloaded Songs 🎶")
        
        # Define directory where preloaded songs should be
        songs_dir = "preloaded_songs"
        
        # Check if directory exists, if not, create it (for testing)
        if not os.path.exists(songs_dir):
            st.error(f"Directory '{songs_dir}' does not exist. Please add your music files to this folder.")
            return

        # List all .mp3 or .wav files in the directory
        songs = [f for f in os.listdir(songs_dir) if f.endswith(".mp3") or f.endswith(".wav")]
        
        if songs:
            song_names = [os.path.splitext(song)[0] for song in songs]
            # Let user select a song from the preloaded list
            selected_song = st.selectbox("Choose a song to play", song_names)
            if selected_song:
               st.audio(os.path.join(songs_dir, selected_song + os.path.splitext(songs[0])[1]), format="audio/mp3", start_time=0)
        else:
            st.write("No songs found in the preloaded_songs directory. Please add MP3/WAV files.")

    # Handle Upload Your Song
    elif option == "Upload Your Song":
        st.subheader("Upload Your Song 🎤")
        uploaded_file = st.file_uploader("Upload a song (MP3/WAV)", type=["mp3", "wav"])

        if uploaded_file is not None:
            try:
                # Ensure the file is either MP3 or WAV
                file_format = uploaded_file.name.split('.')[-1].lower()
                if file_format in ["mp3", "wav"]:
                    st.audio(uploaded_file, format=f"audio/{file_format}", start_time=0)
                else:
                    st.error("Unsupported file format. Please upload MP3 or WAV files.")
            except Exception as e:
                st.error(f"Error playing audio: {e}")

if __name__ == "__main__":
    main()
