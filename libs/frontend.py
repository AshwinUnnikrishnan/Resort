import streamlit as st


def sidebar_set():
    """
    Set up file upload sections in the Streamlit sidebar for uploading video and JSON data.

    Returns:
        tuple: A tuple containing the uploaded video file and JSON file.

    Example:
        video, json_data = sidebar_set()
    """
    # File upload section for video
    st.sidebar.title("Upload Video")
    video_file = st.sidebar.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])

    # File upload section for JSON data
    st.sidebar.title("Upload JSON Data")
    json_file = st.sidebar.file_uploader("Choose a JSON file", type=["json"])

    return video_file, json_file