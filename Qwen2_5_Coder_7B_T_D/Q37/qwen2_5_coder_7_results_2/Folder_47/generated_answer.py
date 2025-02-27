def filter_chars(s):
    chars_to_remove = set([chr(i) for i in range(ord(':'), ord('r') + 1)])
    return ''.join([c for c in s if not (38 <= s.index(c) <= 54 and c in chars_to_remove)])