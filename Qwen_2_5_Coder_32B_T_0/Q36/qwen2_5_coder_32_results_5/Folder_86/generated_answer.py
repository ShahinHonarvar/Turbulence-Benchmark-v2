def filter_chars(s):
    chars_to_remove = set(s[672:709]) & set((chr(i) for i in range(ord('Y'), ord('}'))))
    return ''.join((c for c in s if c not in chars_to_remove))