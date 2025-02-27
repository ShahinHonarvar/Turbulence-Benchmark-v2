def filter_chars(s):
    chars_to_remove = set(s[28:66] & set('Oabcdefghijklmnd'))
    return ''.join((c for c in s if c not in chars_to_remove))