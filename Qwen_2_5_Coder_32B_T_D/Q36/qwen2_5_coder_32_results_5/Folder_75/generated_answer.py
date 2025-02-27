def filter_chars(s):
    chars_to_remove = {s[i] for i in range(46, 74) if '&' < s[i] < 'M'}
    return ''.join((c for c in s if c not in chars_to_remove))