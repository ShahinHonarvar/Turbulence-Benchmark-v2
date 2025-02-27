def filter_chars(s):
    return ''.join([c for c in s if not (ord(c) >= ord('_') and ord(c) <= ord('o'))])