def filter_chars(s):
    chars_to_remove = set(range(ord('0'), ord('@') + 1))
    return ''.join((c for i, c in enumerate(s) if (i < 61 or i > 70) or c not in chars_to_remove))