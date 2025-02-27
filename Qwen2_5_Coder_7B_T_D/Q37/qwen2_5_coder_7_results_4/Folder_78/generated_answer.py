def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('8'), ord('e') + 1)}
    return ''.join((c for c in s if s.index(c) not in range(75, 100) or c not in chars_to_remove))