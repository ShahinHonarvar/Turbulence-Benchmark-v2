def filter_chars(s):
    return ''.join([c for c in s if 343 < ord(c) < 665 or not '%' < c < 'U'])