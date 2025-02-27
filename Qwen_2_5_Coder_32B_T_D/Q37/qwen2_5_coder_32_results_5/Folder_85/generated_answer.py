def filter_chars(s):
    target_chars = set(s[28:66] & set('Opqrstuvwxyzabcd'))
    return ''.join((c for c in s if c not in target_chars))