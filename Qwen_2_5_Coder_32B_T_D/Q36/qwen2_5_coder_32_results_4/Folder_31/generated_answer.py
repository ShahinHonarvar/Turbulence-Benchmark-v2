def filter_chars(s):
    chars_to_remove = {s[i] for i in range(14, 75) if '9' < s[i] < 'K'}
    return ''.join((c for c in s if c not in chars_to_remove))