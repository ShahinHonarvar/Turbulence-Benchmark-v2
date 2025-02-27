def return_nth_smallest_ascii(string):
    """
    This function takes a string of distinct characters as input,
    and returns the character with the 16th smallest ASCII value
    among those characters that occur between indices 46 and 82,
    both inclusive.
    """
    sorted_string = sorted(string)
    return sorted_string[15]