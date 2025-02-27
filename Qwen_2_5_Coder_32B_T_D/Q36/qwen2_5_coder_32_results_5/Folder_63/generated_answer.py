def filter_chars(s):
    chars_to_remove = set(s[26:80]) & set('<>[]^_`{|}~')
    return ''.join((c for c in s if c not in chars_to_remove))