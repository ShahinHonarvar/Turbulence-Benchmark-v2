def filter_chars(text):
    return ''.join([c for c in text if c < 'm' or c > 'w' or text.index(c) < 25 or (text.index(c) > 97)])