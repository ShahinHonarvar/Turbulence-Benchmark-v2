def filter_chars(string):
    return ''.join([c for c in string if (ord(c) < ord('K') or ord(c) > ord('z')) or (string.index(c) < 29 or string.index(c) > 79)])