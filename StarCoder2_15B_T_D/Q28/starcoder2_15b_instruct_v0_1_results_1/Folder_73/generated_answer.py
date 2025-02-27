def return_nth_smallest_ascii(s):
    """
    Returns the character with the 10th smallest ASCII value among those
    characters in the string `s` that occur between indices 0 to 69, both inclusive.
    """
    chars = [c for c in s[0:70]]
    chars.sort(key=lambda c: ord(c))
    return chars[9]