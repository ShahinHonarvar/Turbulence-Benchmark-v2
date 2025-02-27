def filter_chars(s):
    chars_to_remove = {s[i] for i in range(10, 53) if '@' <= s[i] <= 'T'}
    return ''.join((c for c in s if c not in chars_to_remove))