"""
Object Detection relation functions.
get_chair_bounding_polygon : reads the json to get chair bounding polygons.
detect_objects_yolo : runs YOLO model
get_person_bounding_polygon : get person bounding points
detect_objects_get_bounding_polygon : Perform detection and get person and return person bounding boxes
"""

import json
import numpy as np


def get_chair_bounding_polygon(uploaded_file):
    """
    Load JSON data containing bounding polygon information and extract chair details.

    Parameters:
        uploaded_file (str): The file generated from roboflow after manually drawing the bounding polygon.

    Returns:
        list of numpy.ndarray: A list of arrays containing the bounding polygon points for chairs.

    Raises:
        JSONDecodeError: If the JSON file cannot be decoded.
    """
    try:

        file_content = uploaded_file.read().decode("utf-8")

        # Parse the JSON content into a dictionary
        json_data = json.loads(file_content)

        # Extract bounding polygon points for chairs
        chair_bounding_polygon_points = [np.array(boxes['points']) for boxes in json_data['boxes']]

        return chair_bounding_polygon_points

    except json.JSONDecodeError:
        # Raise an error if the JSON content cannot be decoded
        raise json.JSONDecodeError("Unable to decode JSON content.")


def detect_objects_yolo(image_array, model):
    """
    Detect objects in an image using the YOLO model.

    Parameters:
        image_array (numpy.ndarray): The input image as a NumPy array.
        model: The YOLO model used for object detection.

    Returns:
        list: A list of detected objects along with their bounding boxes and confidence scores.
    """
    # Perform object detection on the image using the YOLO model
    results = model.predict(image_array)[0]
    return results


def get_person_bounding_polygon(results):
    """
    Extracts the bounding polygons of all detected persons.

    Parameters:
        results: Object containing detection results.

    Returns:
        list of numpy.ndarray: List of bounding polygons for all detected persons.

    Note:
        The 'results' object is expected to contain the following attributes:
            - names: List of class names.
            - boxes: Object containing bounding box coordinates.
            - masks: Object containing mask coordinates.

    Example:
        results = YOLO_model.predict(image)
        person_bounding_polygons = get_person_bounding_polygon(results)
    """
    # Extract class names and detected objects
    classes = results.names
    detected_objects = results.boxes.cls.tolist()

    all_person_masks = []

    for i in range(len(detected_objects)):

        if classes[detected_objects[i]] == "person":
            mask = results.masks.xy[i]
            all_person_masks.append(mask)

    return all_person_masks


def detect_objects_get_bounding_polygon(image_array, model):
    """
    Detect objects in an image using the provided YOLO model and extract bounding polygons of persons.

    Parameters:
        image_array (numpy.ndarray): The input image as a NumPy array.
        model: The YOLO model used for object detection.

    Returns:
        list of numpy.ndarray: A list containing the bounding polygons of all detected persons.

    Raises:
        ValueError: If the input image is not provided or is in an invalid format.
        RuntimeError: If there's an issue with the YOLO model or object detection process.

    Example:
        >>> model = YOLOModel()
        >>> image = load_image("image.jpg")
        >>> person_bounding_polygons = detect_objects_get_bounding_polygon(image, model)
    """
    if image_array is None or not isinstance(image_array, np.ndarray):
        raise ValueError("Input image must be provided as a valid NumPy array.")

    try:
        # Perform object detection on the input image using the YOLO model
        detection_results = detect_objects_yolo(image_array, model)
    except Exception as e:
        raise RuntimeError("Error occurred during object detection process.") from e

    try:
        # Extract bounding polygons of all detected persons from the detection results
        all_person_bounding_polygon = get_person_bounding_polygon(detection_results)
    except Exception as e:
        raise RuntimeError("Error occurred while extracting person bounding polygons.") from e

    return all_person_bounding_polygon