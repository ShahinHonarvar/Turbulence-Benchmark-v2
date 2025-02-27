def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i not in range(3, 5) or not 'Y' < c < 's'))