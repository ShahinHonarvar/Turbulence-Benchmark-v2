def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if i < 31 or i > 73 or (not ord('M') < ord(c) < ord('j'))])