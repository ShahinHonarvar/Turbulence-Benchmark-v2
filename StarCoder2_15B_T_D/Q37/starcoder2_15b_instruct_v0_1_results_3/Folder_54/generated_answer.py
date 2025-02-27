def filter_chars(s):
    return ''.join((c for c in s if not (46 <= ord(c) <= 85 and ord(c) >= ord('-') and (ord(c) <= ord('X')))))