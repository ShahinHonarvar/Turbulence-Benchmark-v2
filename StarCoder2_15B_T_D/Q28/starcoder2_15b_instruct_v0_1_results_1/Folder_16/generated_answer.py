def return_nth_smallest_ascii(string):
    """
    Returns the character with the 7th smallest ASCII value among those characters
    in the string that occur between indices 18 to 45, both inclusive.
    """
    substring = string[18:46]
    sorted_substring = sorted(substring)
    return sorted_substring[6]