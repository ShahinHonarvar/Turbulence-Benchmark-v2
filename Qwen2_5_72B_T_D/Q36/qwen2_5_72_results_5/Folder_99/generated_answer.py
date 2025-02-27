def filter_chars(s):
    to_remove = {s[i] for i in range(476, 948) if 'b' < s[i] < 'd'}
    return ''.join((c for c in s if c not in to_remove))