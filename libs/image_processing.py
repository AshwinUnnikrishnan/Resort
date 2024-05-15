import numpy as np
import cv2
import tempfile


def plot_image_with_bounding_polygon(image_array, all_person_bounding_polygon, chair_bounding_polygon_points, overlaps):
    """
    Plot the input image with bounding polygons for people and chairs.

    Parameters:
        image_array (numpy.ndarray): The input image as a NumPy array.
        all_person_bounding_polygon (list of numpy.ndarray): List of bounding polygons for all detected persons.
        chair_bounding_polygon_points (list of numpy.ndarray): List of bounding polygons for all chairs.
        overlaps (list of tuple): List of detected overlaps between chairs and people.

    Returns:
        numpy.ndarray: Image with bounding polygons drawn.

    Example:
        img_with_polygons = plot_image_with_bounding_polygon(image, person_bounding_polygons, chair_bounding_polygons, overlaps)
    """
    img_with_polygons = np.copy(image_array)  # Create a copy of the original image

    # Draw polygons for all person bounding polygons
    for coordinates in all_person_bounding_polygon:
        coordinates = coordinates.astype(np.int32)
        cv2.polylines(img_with_polygons, [coordinates], isClosed=True, color=(0, 0, 255), thickness=2)

    # Draw polygons for chair bounding polygons
    for i, coordinates in enumerate(chair_bounding_polygon_points):
        coordinates = coordinates.astype(np.int32)
        color = (255, 0, 0) if i in [pair[0] for pair in overlaps] else (0, 255, 0)
        cv2.polylines(img_with_polygons, [coordinates], isClosed=True, color=color, thickness=2)
        cv2.putText(img_with_polygons, f'Chair {i}', tuple(coordinates[0]), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    return img_with_polygons


def create_video_from_frames(frames, output_video_path, fps):
    """
    Create a video from a list of frames.

    Parameters:
        frames (list of numpy.ndarray): List of frames as NumPy arrays.
        output_video_path (str): Path to save the output video file.
        fps (float): Frames per second for the output video.

    Returns:
        None

    Example:
        create_video_from_frames(frame_list, 'output.mp4', 30)
    """
    height, width, _ = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    for frame in frames:
        video.write(frame)

    video.release()

def create_temp_file(video_file):
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())
    return tfile.name