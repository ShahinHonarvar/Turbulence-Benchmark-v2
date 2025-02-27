def return_nth_smallest_ascii(s: str) -> str:
    """
    Returns the character with the 11th smallest ASCII value among those
    characters in the string `s` that occur between indices 21 to 59, both inclusive.
    """
    filtered_chars = sorted({ch for ch in s[21:60]})
    return filtered_chars[10]