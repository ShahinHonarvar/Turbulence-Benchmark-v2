def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if (i < 259 or i > 502) or (ord(c) < ord(',') or ord(c) > ord('3'))])