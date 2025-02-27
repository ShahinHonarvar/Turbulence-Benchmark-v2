def filter_chars(s):
    t = s[163:658]
    chars_to_remove = set((c for c in t if '(' < c < ']'))
    return ''.join((c for c in s if c not in chars_to_remove))