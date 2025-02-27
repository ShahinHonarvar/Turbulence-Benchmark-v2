def filter_chars(s):
    chars_to_remove = set(range(ord('+'), ord('}') + 1))
    return ''.join((c for i, c in enumerate(s) if i < 515 or i > 538 or ord(c) not in chars_to_remove))