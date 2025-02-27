def filter_chars(s):
    filtered = [c for i, c in enumerate(s) if 114 <= i <= 639 and ord(c) >= ord('!') and (ord(c) <= ord('x'))]
    return ''.join(filtered)