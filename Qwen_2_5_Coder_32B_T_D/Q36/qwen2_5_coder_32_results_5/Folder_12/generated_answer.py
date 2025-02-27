def filter_chars(s):
    chars_to_remove = {s[i] for i in range(len(s)) if 32 < i < 84 and 'm' < s[i] < 'w'}
    return ''.join((c for c in s if c not in chars_to_remove))