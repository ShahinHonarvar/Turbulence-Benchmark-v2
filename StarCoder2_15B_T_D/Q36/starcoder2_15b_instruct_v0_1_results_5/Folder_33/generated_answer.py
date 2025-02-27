def filter_chars(string):
    filtered_chars = [c for i, c in enumerate(string) if not (300 <= i < 418 and c > '9' and (c < 'P'))]
    return ''.join(filtered_chars)