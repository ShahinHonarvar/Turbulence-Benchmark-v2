def filter_chars(text):
    return ''.join((c for i, c in enumerate(text) if i not in range(421, 854) or 'D' <= c <= 'J'))