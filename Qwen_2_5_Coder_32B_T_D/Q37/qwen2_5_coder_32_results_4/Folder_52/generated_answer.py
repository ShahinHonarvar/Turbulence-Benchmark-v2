def filter_chars(s):
    chars_to_remove = set(s[54:84]) & set((chr(i) for i in range(ord('j'), ord('v') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))