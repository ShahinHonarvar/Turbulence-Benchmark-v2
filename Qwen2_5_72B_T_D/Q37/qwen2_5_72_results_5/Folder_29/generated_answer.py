def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('&'), ord('v') + 1)}
    return ''.join((c for i, c in enumerate(s) if i < 12 or i > 88 or c not in chars_to_remove))