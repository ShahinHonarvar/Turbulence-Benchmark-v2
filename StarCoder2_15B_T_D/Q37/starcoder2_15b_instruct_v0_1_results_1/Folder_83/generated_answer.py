def filter_chars(text):
    return ''.join((c for c in text if c < 'K' or c > 'z' or (c < 'a' and c > 'K')))