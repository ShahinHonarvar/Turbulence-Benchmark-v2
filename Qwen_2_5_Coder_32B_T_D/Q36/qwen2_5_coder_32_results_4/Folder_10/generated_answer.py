def filter_chars(s):
    chars_to_remove = set(s[35:60]) & set([chr(i) for i in range(ord('!') + 1, ord('B'))])
    return ''.join((c for c in s if c not in chars_to_remove))