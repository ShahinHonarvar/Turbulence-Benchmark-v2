def return_nth_smallest_ascii(s: str) -> str:
    """
    Returns the character with the 20th smallest ASCII value among those characters
    in the string that occur between indices 34 to 85, both inclusive.
    """
    chars = [c for c in s[34:86]]
    sorted_chars = sorted(chars, key=lambda c: ord(c))
    return sorted_chars[19]