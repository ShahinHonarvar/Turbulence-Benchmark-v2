def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('2'), ord('s') + 1)}
    return ''.join((c for c in s if 36 <= s.index(c) <= 79 and c not in chars_to_remove or c not in chars_to_remove))