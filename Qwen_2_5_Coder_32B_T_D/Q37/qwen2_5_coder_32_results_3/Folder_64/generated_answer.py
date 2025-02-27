def filter_chars(s):
    chars_to_remove = set(s[1:8]) & set((chr(x) for x in range(ord('L'), ord('a') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))