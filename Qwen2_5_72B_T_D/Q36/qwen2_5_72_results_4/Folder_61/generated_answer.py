def filter_chars(s):
    to_remove = {s[i] for i in range(3, 9) if '*' < s[i] < 'E'}
    return ''.join((c for c in s if c not in to_remove))