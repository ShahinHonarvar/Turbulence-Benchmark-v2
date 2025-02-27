def filter_chars(s):
    chars_to_remove = set(range(ord('/'), ord('9') + 1))
    result = ''.join((c for i, c in enumerate(s) if i < 384 or i > 411 or ord(c) not in chars_to_remove))
    return result