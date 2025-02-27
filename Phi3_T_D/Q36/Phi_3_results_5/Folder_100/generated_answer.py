def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if not (43 < ord(c) < ord('r') and 43 < i < 69)])