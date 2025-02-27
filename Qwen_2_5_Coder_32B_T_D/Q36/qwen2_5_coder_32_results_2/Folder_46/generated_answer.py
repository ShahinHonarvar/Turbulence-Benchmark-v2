def filter_chars(s):
    if len(s) <= 69:
        return s
    chars_to_remove = {s[i] for i in range(19, 69) if '<' < s[i] < 'C'}
    return ''.join((c for c in s if c not in chars_to_remove))