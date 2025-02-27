def filter_chars(s):
    return ''.join([c for c in s if not 32 < ord(c) < ord('D')])