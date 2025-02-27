def filter_chars(s):
    chars_to_remove = set(s[219:403])
    chars_to_remove = {c for c in chars_to_remove if '*' < c < '7'}
    return ''.join((c for c in s if c not in chars_to_remove))