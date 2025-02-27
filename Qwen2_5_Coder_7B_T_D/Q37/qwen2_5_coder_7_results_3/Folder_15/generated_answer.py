def filter_chars(s):
    chars_to_remove = set(range(ord('?'), ord('f') + 1))
    return ''.join((ch for ch in s if ch < '2' or ch > '6' or ord(ch) not in chars_to_remove))