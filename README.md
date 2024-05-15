---
title: Resort
emoji: 📉
colorFrom: indigo
colorTo: yellow
sdk: streamlit
pinned: false
app_file: streamlit_main.py
app_port: 8501
license: apache-2.0
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
---

# Live Resort Pool Chair Monitoring

Live Monitoring is an application designed for real-time monitoring of video feeds, particularly focusing on detecting people and their interactions with chairs. This README provides an overview of the project, including setup instructions, usage guidelines, functionality details, contributors, and licensing information.

## Table of Contents

- [Introduction](#introduction)

- [Setup](#setup)

- [Usage](#usage)

- [Functionality](#functionality)

- [Contributors](#contributors)

## Introduction

Live Monitoring employs object detection techniques to analyze video streams, identifying individuals (people) and objects (chairs) within each frame. By detecting interactions between people and chairs, the application facilitates occupancy management, enabling real-time monitoring and analysis of seating arrangements.

## Setup

To run the Live Monitoring application, follow these steps:

1\. Install the required dependencies by executing the following command in your terminal:

    ```

    pip install -r requirements.txt

    ```

    Make sure to replace `requirements.txt` with the appropriate file containing the dependencies for your environment.

2\. Ensure that you have a compatible video file and a corresponding JSON file containing chair bounding polygon information. The JSON file can be created using Roboflow for manual bounding polygon annotation.

3\. Run the Streamlit application by executing the `start()` function in the `main.py` file.

## Usage

Once the application is set up and running, follow these steps to utilize Live Monitoring:

1\. Upload a video file and its corresponding JSON file containing chair bounding polygon information.

2\. Click the "Process" button within the Streamlit application to initiate live monitoring of the video feed.

3\. The application will display processed frames in real-time, highlighting detected people and their interactions with chairs.

## Functionality

Live Monitoring offers the following key functionalities:

- **Object Detection**: Utilizes the YOLO (You Only Look Once) model for real-time object detection, identifying people and chairs within video frames.

- **Overlap Detection**: Calculates overlaps between detected people and chair bounding polygons to manage chair occupancy effectively.

- **Occupancy Management**: Tracks chair occupancy based on detected overlaps, updating the status of each chair dynamically.

- **Live Monitoring**: Provides a user-friendly interface for real-time display of video frames, with overlaid bounding polygons for people and chairs.

## Contributors

This project was developed by Ashwin Unnikrishnan.
---

Feel free to customize this README further or provide additional information specific to your project's requirements. Let me know if you need further assistance or have any specific preferences!
