def remove_repeat_chars(string):
    """
    Remove repeated characters from a string between indices 100 and 200 (exclusive).
    """
    chars = [c for i, c in enumerate(string) if i < 100 or i >= 200 or string.count(c) == 1]
    return ''.join(chars)