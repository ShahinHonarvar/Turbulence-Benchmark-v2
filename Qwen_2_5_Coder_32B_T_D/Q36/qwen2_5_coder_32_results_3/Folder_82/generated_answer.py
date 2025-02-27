def filter_chars(s):
    chars_to_remove = set(s[69:97]) & set([chr(i) for i in range(ord('W'), ord('j'))])
    return ''.join((c for c in s if c not in chars_to_remove))