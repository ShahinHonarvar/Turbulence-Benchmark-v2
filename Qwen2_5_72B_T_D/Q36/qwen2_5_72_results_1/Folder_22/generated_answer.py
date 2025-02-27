def filter_chars(s):
    to_remove = {s[i] for i in range(55, 84) if ';' < s[i] < 'z'}
    return ''.join((c for c in s if c not in to_remove))