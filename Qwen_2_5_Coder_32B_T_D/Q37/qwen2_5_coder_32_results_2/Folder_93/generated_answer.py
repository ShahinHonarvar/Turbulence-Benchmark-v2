def filter_chars(s):
    chars_to_remove = set(s[38:70] & set('H tÃ©lÃ©phone'))
    return ''.join((c for c in s if c not in chars_to_remove))