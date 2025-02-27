def filter_chars(s):
    filtered_chars = [c for j, c in enumerate(s) if not (299 < j < 418 and '9' < c < 'P')]
    return ''.join(filtered_chars)