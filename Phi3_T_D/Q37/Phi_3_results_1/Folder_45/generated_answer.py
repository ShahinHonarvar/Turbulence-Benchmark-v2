def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if not (72 <= i <= 94 and ord(c) >= ord('.') and (ord(c) <= ord('b')))])