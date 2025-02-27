def filter_chars(s):
    to_remove = set()
    for i in range(26, 65):
        if 'V' <= s[i] <= 'o':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))