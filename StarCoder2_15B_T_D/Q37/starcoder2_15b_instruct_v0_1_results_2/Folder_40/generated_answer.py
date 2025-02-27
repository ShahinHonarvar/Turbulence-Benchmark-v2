def filter_chars(text):
    return ''.join((c for c in text if not 0 <= ord(c) - ord('*') <= 1))