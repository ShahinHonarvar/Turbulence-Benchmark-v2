def filter_chars(s):
    chars_to_remove = set(s[2:4]) & set([chr(i) for i in range(ord('5'), ord('_') + 1)])
    return ''.join([c for c in s if c not in chars_to_remove])