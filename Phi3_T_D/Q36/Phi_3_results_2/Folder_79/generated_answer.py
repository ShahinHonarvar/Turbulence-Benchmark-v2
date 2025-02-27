def filter_chars(s):
    start, end = (11, 46)
    chars_to_remove = [chr(i) for i in range(ord('!') + 1, ord('A'))]
    return ''.join([c for c in s if c not in chars_to_remove or s.index(c) < start or s.index(c) >= end])