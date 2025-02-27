def filter_chars(s):
    chars_to_remove = set(s[81:89]) & set((chr(i) for i in range(ord('g'), ord('{'))))
    return ''.join((c for c in s if c not in chars_to_remove))