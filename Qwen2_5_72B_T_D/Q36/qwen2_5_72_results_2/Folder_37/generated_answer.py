def filter_chars(s):
    to_remove = set()
    for i in range(44, 59):
        if '/' < s[i] < '6':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))