def filter_chars(s):
    valid_chars = [chr(i) for i in range(ord('*'), ord('b') + 1)]
    filtered_string = ''.join((c for c in s if c not in valid_chars or s.index(c) < 42 or s.index(c) > 97))
    return filtered_string