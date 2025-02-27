def filter_chars(s):
    """Filter chars in a string."""
    filtered = [c for c in s if not 1 < ord(c) - ord('-') < 7]
    return ''.join(filtered)