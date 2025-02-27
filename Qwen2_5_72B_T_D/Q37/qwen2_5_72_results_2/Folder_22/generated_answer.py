def filter_chars(s):
    to_remove = set()
    for i in range(33, 71):
        if '7' <= s[i] <= 'k':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))