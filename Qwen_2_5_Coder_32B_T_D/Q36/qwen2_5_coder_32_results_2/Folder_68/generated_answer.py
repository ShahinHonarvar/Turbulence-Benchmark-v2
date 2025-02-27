def filter_chars(s):
    chars_to_remove = {s[i] for i in range(2, 9) if '8' < s[i] < 'm'}
    return ''.join((c for c in s if c not in chars_to_remove))