def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('S'), ord('s') + 1)}
    return ''.join((ch for ch in s if s.index(ch) < 41 or s.index(ch) > 86 or ch not in chars_to_remove))