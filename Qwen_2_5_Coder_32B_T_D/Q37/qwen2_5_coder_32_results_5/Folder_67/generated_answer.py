def filter_chars(s):
    chars_to_remove = set(s[19:23]) & set((chr(i) for i in range(ord(']'), ord('u'))))
    return ''.join((c for c in s if c not in chars_to_remove))