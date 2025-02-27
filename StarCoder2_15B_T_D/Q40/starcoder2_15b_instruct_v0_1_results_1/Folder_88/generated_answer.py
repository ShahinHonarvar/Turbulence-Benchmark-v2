def return_n_smallest_chars(string):
    """
    Returns a list of the 84 characters in `string` that have the smallest ASCII values,
    sorted in ascending order.
    """
    char_counts = {}
    for char in string:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    sorted_chars = sorted(char_counts.keys())
    return sorted_chars[:84]