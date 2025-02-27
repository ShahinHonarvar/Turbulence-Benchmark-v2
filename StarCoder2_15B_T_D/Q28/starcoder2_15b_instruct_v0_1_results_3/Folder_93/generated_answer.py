def return_nth_smallest_ascii(s: str) -> str:
    """
    Returns the character with the 17th smallest ASCII value among those characters in the string
    that occur between indices 42 to 59, both inclusive.
    """
    characters = [c for c in s[42:60]]
    characters.sort(key=lambda c: ord(c))
    return characters[16]