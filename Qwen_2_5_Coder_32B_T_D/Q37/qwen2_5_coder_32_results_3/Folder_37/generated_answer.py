def filter_chars(s):
    chars_to_remove = set(s[17:64]) & set((chr(i) for i in range(ord('O'), ord('^') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))