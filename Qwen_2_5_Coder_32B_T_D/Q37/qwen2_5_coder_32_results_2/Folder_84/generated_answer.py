def filter_chars(s):
    chars_to_remove = set(s[138:921] & set((chr(i) for i in range(ord('6'), ord('A') + 1))))
    return ''.join((c for c in s if c not in chars_to_remove))