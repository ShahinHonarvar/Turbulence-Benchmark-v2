def return_nth_smallest_ascii(string):
    """
    Returns the character with the 13th smallest ASCII value among those
    characters in the string that occur between indices 0 to 18, both inclusive.
    """
    sorted_string = sorted(string[0:19])
    return sorted_string[12]