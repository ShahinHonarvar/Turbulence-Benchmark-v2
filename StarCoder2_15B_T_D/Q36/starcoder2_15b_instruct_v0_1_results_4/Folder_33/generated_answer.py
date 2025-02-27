def filter_chars(text):
    return ''.join([c for i, c in enumerate(text) if i < 299 or i >= 418 or (not '9' < c < 'P')])