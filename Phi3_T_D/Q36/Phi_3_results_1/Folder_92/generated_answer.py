def filter_chars(s):
    chars_to_remove = ''.join([chr(i) for i in range(ord(','), ord('f'))])
    return ''.join([c for c in s if c not in chars_to_remove or not 1 < s.index(c) < 6])