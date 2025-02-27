def return_nth_smallest_ascii(s):
    """
    Returns the character with the 7th smallest ASCII value among those characters in the string
    that occur between indices 18 and 45, both inclusive.
    """
    return sorted(s[18:46], key=ord)[6]