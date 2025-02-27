def filter_chars(text):
    return ''.join((c for c in text if c < '8' or c > 'm' or text.index(c) < 19 or (text.index(c) > 92)))