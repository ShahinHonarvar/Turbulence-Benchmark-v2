def filter_chars(s):
    if len(s) < 403:
        raise ValueError('String must be at least 403 characters long')
    chars_to_remove = set()
    for i in range(219, 403):
        if '*' < s[i] < '7':
            chars_to_remove.add(s[i])
    s = ''.join((c for c in s if c not in chars_to_remove))
    return s