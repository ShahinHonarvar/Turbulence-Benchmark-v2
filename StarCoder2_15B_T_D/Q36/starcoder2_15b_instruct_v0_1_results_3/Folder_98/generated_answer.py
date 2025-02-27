def filter_chars(string):
    return ''.join([c for i, c in enumerate(string) if i < 4 or i >= 8 or (not (ord(c) > ord('1') and ord(c) < ord('J')))])