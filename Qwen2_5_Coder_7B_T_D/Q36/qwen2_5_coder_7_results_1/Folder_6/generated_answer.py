def filter_chars(s):
    chars = [c for c in s if not (31 < ord(c) < 70 and 'B' < c < 'v')]
    return ''.join(chars)