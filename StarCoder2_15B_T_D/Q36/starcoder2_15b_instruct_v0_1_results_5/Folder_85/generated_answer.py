def filter_chars(text):
    return ''.join((c for c in text if c <= 'S' or c >= 's' or ord(c) < 55 or (ord(c) >= 80)))