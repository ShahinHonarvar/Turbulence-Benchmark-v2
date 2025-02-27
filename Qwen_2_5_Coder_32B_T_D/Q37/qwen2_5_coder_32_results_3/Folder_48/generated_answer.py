def filter_chars(s):
    if len(s) < 878:
        return s
    chars_to_remove = set(s[513:878])
    chars_to_remove = {c for c in chars_to_remove if '?' <= c <= 'n'}
    return ''.join((c for c in s if c not in chars_to_remove))