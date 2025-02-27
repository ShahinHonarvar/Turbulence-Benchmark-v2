def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 344 or i > 874 or ord('f') <= ord(c) <= ord('~')))