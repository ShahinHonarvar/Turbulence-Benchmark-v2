def filter_chars(s):
    chars_to_remove = set(s[384:412]) & set('/012345678')
    return ''.join((c for c in s if c not in chars_to_remove))