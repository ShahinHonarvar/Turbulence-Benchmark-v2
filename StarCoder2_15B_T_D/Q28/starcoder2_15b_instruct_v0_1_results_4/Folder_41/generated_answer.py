def return_nth_smallest_ascii(s):
    """Returns the character with the 19th smallest ASCII value among those characters in the string that occur between indices 58 to 85, both inclusive."""
    sorted_chars = sorted(s[58:86])
    return sorted_chars[18]