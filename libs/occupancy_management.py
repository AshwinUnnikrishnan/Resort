def increment_chair_occupancy(chair_occupancy, overlaps, chairs_len):
    """
    Increment chair occupancy based on detected overlaps.

    Parameters:
        chair_occupancy (dict): Dictionary containing chair occupancy counts.
        overlaps (list of tuples): List of detected overlaps between chairs and people.
        chairs_len (int): Total number of chairs.

    Returns:
        tuple: Updated list of overlaps and chair occupancy dictionary.
    """
    chairs = []
    for chair_id, people_id in overlaps:
        chair_occupancy[chair_id] += 1
        chairs.append(chair_id)

    for chair_id in range(chairs_len):
        if chair_id not in chairs:
            chair_occupancy[chair_id] = 0
    updated_overlap = []
    for overlap in overlaps:
        if chair_occupancy[overlap[0]] > 4:
            updated_overlap.append(overlap)
    return updated_overlap, chair_occupancy