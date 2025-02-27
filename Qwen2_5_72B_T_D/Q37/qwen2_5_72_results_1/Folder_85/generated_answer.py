def filter_chars(s):
    to_remove = set()
    for i in range(28, 66):
        if 'O' <= s[i] <= 'd':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))