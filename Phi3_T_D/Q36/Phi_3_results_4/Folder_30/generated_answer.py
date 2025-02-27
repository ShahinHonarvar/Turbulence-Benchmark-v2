def filter_chars(s):
    new_s = ''.join((c for i, c in enumerate(s) if not (23 < i < 45 and '3' < c < 'I')))
    return new_s