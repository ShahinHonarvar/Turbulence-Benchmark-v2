def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 72 or i >= 93 or (not (ord(c) > ord('<') and ord(c) < ord('J')))))