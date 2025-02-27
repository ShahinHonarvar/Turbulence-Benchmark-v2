def filter_chars(s):
    chars_to_remove = set(s[38:70])
    chars_to_remove = {c for c in chars_to_remove if 'H' <= c <= 'e'}
    return ''.join((c for c in s if c not in chars_to_remove))