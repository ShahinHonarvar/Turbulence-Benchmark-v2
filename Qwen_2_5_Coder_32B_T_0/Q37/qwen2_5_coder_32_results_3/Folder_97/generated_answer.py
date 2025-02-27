def filter_chars(s):
    chars_to_remove = set(s[227:236]) & set((chr(i) for i in range(ord('D'), ord('u') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))