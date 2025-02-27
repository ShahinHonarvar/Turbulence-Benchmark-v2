def return_nth_smallest_ascii(s: str) -> str:
    """
    Returns the character with the 6th smallest ASCII value among those characters in the string
    that occur between indices 15 and 21, both inclusive.
    """
    chars = [c for c in s[15:22]]
    chars.sort(key=lambda x: ord(x))
    return chars[5]