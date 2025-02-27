def return_nth_smallest_ascii(s: str) -> str:
    """
    Returns the character with the 13th smallest ASCII value among those characters
    in the string that occur between indices 5 and 47, both inclusive.
    """
    return sorted(s[5:48])[12]