import time
import cv2
import numpy as np
import streamlit as st
from ultralytics import YOLO
from libs.object_detection import detect_objects_get_bounding_polygon, get_chair_bounding_polygon
from config.config import *
from libs.image_processing import create_temp_file, plot_image_with_bounding_polygon
from libs.polygon_calculation import calculate_overlap_images
from libs.occupancy_management import increment_chair_occupancy
from libs.frontend import sidebar_set


def live_monitoring(video_file, json_file, img_placeholder):
    """
    Live monitoring function to process video frames in real-time and display the results.

    Parameters:
        video_file (str): Path to the video file.
        json_file (str): Path to the json file.
        img_placeholder (streamlit.delta_generator.DeltaGenerator): Streamlit image placeholder for displaying frames.

    Returns:
        None
    """
    video = create_temp_file(video_file)  # loads and create a tempfile in memory, will be replaced by camera port
    cap = cv2.VideoCapture(video)
    fps = cap.get(cv2.CAP_PROP_FPS)

    model = YOLO(MODEL_PATH)

    # Get the bounding boxes for the camera
    chair_bounding_polygon_points = get_chair_bounding_polygon(json_file)

    # to maintain the chair availability
    chair_occupancy = {key: 0 for key in range(len(chair_bounding_polygon_points))}

    count = 0  # count frames
    output_frames = []
    start_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        fps_rem = count % fps
        if fps_rem == 0 or fps_rem == 4:
            frame_array = np.array(frame)
            # run the frame to detect people
            people = detect_objects_get_bounding_polygon(frame_array, model)

            # based on the people polygons and chairs find overlaps
            overlaps = calculate_overlap_images(chair_bounding_polygon_points, people)

            # update the overlap based on chair occupancy only get if overlap for last 10 frames
            overlaps, chair_occupancy = increment_chair_occupancy(chair_occupancy, overlaps,
                                                                  len(chair_bounding_polygon_points))
            # check if the chairs have been overlapped in last 10 frames only then make it unavailable
            image = plot_image_with_bounding_polygon(frame_array, people, chair_bounding_polygon_points, overlaps)
            output_frames.append(image)
            img_placeholder.image(image)

        count += 1
    cap.release()
    cv2.destroyAllWindows()
    end_time = time.time()
    print("Time taken:", end_time - start_time)

    return


def start():
    """
    Streamlit app entry point. Sets up the UI and triggers video processing when the 'Process' button is clicked.
    """
    st.title("Live Monitoring")

    video_file, json_file = sidebar_set()

    if video_file is not None and json_file is not None:

        img_placeholder = st.empty()

        if st.sidebar.button("Process"):
            live_monitoring(video_file, json_file, img_placeholder)


if __name__ == "__main__":
    start()
