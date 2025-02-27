def filter_chars(s):
    if len(s) <= 639:
        return s
    chars_to_remove = set(s[114:640])
    chars_to_remove = {c for c in chars_to_remove if '!' <= c <= 'x'}
    return ''.join((c for c in s if c not in chars_to_remove))