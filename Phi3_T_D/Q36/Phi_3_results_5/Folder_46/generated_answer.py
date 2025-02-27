def filter_chars(s):
    altered = [c for i, c in enumerate(s) if not (19 < i < 69 and '<' < c < 'C')]
    return ''.join(altered)