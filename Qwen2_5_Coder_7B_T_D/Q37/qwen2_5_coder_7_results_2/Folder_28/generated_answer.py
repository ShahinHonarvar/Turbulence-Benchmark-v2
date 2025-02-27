def filter_chars(s):
    chars_to_remove = set(range(ord('!'), ord('T') + 1))
    return ''.join((c for c in s if s.index(c) < 20 or s.index(c) > 79 or ord(c) not in chars_to_remove))