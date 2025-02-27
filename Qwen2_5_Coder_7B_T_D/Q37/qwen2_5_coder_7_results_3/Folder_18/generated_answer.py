def filter_chars(s):
    chars_to_remove = set(range(ord('-'), ord('D') + 1))
    return ''.join((c for i, c in enumerate(s) if i < 770 or i > 970 or ord(c) not in chars_to_remove))