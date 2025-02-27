def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not 54 <= i <= 83 or not 'j' <= c <= 'v'))