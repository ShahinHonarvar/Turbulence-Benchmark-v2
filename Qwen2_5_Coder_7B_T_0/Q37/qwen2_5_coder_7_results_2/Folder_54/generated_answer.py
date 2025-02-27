def filter_chars(s):
    chars_to_remove = set(range(ord('-'), ord('X') + 1))
    return ''.join((c for c in s if ord(c) < 46 or ord(c) > 85 or ord(c) not in chars_to_remove))