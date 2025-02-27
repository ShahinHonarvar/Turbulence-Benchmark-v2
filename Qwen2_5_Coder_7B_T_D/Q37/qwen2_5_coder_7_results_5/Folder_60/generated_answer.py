def filter_chars(s):
    chars_to_remove = set(range(ord(':'), ord('L') + 1))
    return ''.join((c for i, c in enumerate(s) if i < 12 or i > 77 or ord(c) not in chars_to_remove))