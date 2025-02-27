def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('!'), ord('s') + 1)}
    return ''.join((c for c in s if s.index(c) not in range(86, 93) or c not in chars_to_remove))