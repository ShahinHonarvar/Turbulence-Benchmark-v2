def filter_chars(s):
    modified_s = ''.join((c for i, c in enumerate(s) if i < 35 or i > 98 or (not 'a' <= c <= 'b')))
    return modified_s