from shapely.geometry import Polygon


def calculate_overlap(poly1_points, poly2_points):
    """
        Calculate the overlap area between two polygons.

        Parameters:
            poly1_points (list of tuples): List of (x, y) coordinates defining the vertices of the first polygon.
            poly2_points (list of tuples): List of (x, y) coordinates defining the vertices of the second polygon.

        Returns:
            float: The area of overlap between the two polygons, or 0.0 if there is no overlap.

        Note:
            This function uses the Shapely library for geometric calculations.

        Example:
            poly1_points = [(0, 0), (0, 1), (1, 1), (1, 0)]  # Coordinates of the first polygon
            poly2_points = [(0.5, 0.5), (0.5, 1.5), (1.5, 1.5), (1.5, 0.5)]  # Coordinates of the second polygon
            overlap_area = calculate_overlap(poly1_points, poly2_points)
    """
    poly1 = Polygon(poly1_points)
    poly2 = Polygon(poly2_points)

    # Calculate the intersection of the two polygons
    intersection = poly1.intersection(poly2)

    if intersection.is_empty:
        return 0.0
    else:
        return intersection.area


def calculate_overlap_images(chair_bounding_polygon_points, people):
    """
    Calculate overlaps between chair bounding polygons and people masks.

    Parameters:
        chair_bounding_polygon_points (list of numpy.ndarray): List of arrays containing chair bounding polygon points.
        people (list of numpy.ndarray): List of arrays containing mask coordinates for people.

    Returns:
        list of tuple: List of tuples indicating overlaps between chairs and people.
            Each tuple contains the indices of the chair and person involved in the overlap.

    Note:
        The function assumes that the 'calculate_overlap' function is defined elsewhere.

    Example:
        chair_bounding_polygons = [...]  # List of chair bounding polygons
        people_masks = [...]  # List of mask coordinates for people
        overlaps = calculate_overlap_images(chair_bounding_polygons, people_masks)
    """
    overlaps = []  # List to store overlaps between chairs and people

    for i in range(len(chair_bounding_polygon_points)):
        for j in range(len(people)):

            overlap_area = calculate_overlap(chair_bounding_polygon_points[i], people[j])
            if overlap_area > 0.5:
                overlaps.append((i, j))

    return overlaps

