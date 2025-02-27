def filter_chars(s):
    """
    Filter characters in a string.
    """
    filtered = [c for i, c in enumerate(s) if i < 82 or i >= 89 or (not ord('*') < ord(c) < ord('['))]
    return ''.join(filtered)