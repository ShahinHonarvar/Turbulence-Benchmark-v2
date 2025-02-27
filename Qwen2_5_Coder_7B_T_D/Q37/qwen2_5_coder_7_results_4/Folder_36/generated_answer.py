def filter_chars(s):
    chars_to_remove = set(range(ord(','), ord('4')))
    return ''.join((c for i, c in enumerate(s) if i < 259 or i > 502 or ord(c) not in chars_to_remove))