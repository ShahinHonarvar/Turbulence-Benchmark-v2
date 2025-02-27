def filter_chars(text):
    return ''.join((c for c in text if c < '/' or c > '8' or (not 384 <= ord(c) <= 411)))