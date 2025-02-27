def filter_chars(s):
    valid_chars = [chr(c) for c in range(ord('O'), ord('^') + 1)]
    filtered_chars = [c for c in s if c not in valid_chars or s.index(c) < 17 or s.index(c) > 63]
    return ''.join(filtered_chars)