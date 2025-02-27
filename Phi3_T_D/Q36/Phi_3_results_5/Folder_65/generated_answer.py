def filter_chars(s):
    return ''.join((c for i, c in enumerate(s, start=0) if not 58 <= i < 82 or not 'F' < c < 'O'))