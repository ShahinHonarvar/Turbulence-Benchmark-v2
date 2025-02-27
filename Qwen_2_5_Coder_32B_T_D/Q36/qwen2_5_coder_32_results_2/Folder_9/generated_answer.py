def filter_chars(s):
    chars_to_remove = set(s[50:92]) & set((chr(i) for i in range(ord('B'), ord('Q'))))
    return ''.join((c for c in s if c not in chars_to_remove))