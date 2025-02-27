def filter_chars(s):
    return ''.join((c for c in s if c < 'V' or c > 'o' or ord(c) < 26 or (ord(c) > 64)))