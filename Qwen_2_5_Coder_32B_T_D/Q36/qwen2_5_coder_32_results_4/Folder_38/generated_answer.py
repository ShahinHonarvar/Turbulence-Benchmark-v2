def filter_chars(s):
    chars_to_remove = {s[i] for i in range(44, 48) if '+' < s[i] < 'l'}
    return ''.join((c for c in s if c not in chars_to_remove))