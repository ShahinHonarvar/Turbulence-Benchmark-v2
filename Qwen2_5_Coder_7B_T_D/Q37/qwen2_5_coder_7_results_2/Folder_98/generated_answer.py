def filter_chars(s):
    chars_to_remove = {chr(x) for x in range(ord('R'), ord('t') + 1)}
    return ''.join((ch for ch in s if ch not in chars_to_remove))