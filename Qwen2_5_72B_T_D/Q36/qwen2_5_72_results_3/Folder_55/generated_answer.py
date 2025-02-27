def filter_chars(s):
    chars_to_remove = {s[i] for i in range(3, 6) if 'Y' < s[i] < 's'}
    return ''.join((c for c in s if c not in chars_to_remove))