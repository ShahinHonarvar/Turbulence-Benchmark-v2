def filter_chars(s):
    chars_to_remove = {s[i] for i in range(29, 98) if '-' <= s[i] <= 'n'}
    return ''.join((c for c in s if c not in chars_to_remove))