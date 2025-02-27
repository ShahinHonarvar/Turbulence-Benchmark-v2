def return_nth_smallest_ascii(s: str) -> str:
    """
    Returns the character with the 11th smallest ASCII value among
    those characters in the string `s` that occur between indices
    20 to 80, both inclusive.
    """
    filtered_chars = [c for i, c in enumerate(s) if 20 <= i <= 80]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[10]