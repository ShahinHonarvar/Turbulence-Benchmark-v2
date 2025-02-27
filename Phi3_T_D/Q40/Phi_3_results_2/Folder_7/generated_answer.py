def return_n_smallest_chars(dist_str: str) -> list:
    """
    Returns a list of the 49 characters with the smallest ASCII values sorted in ascending order.
    :param dist_str: A string of distinct characters.
    :return: List of characters with the smallest ASCII values.
    """
    sorted_chars = sorted(dist_str)
    return sorted_chars[:49]