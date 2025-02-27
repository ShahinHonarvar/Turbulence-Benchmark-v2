def filter_chars(text):
    return ''.join((c for i, c in enumerate(text) if i < 46 or i >= 91 or (not (ord(c) > ord('D') and ord(c) < ord('H')))))