def filter_chars(s):
    chars_to_remove = {s[i] for i in range(77, 87) if ';' < s[i] < 'r'}
    return ''.join((c for c in s if c not in chars_to_remove))