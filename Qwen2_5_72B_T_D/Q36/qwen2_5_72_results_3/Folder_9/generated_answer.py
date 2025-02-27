def filter_chars(s):
    to_remove = set()
    for i in range(50, 92):
        if 'A' < s[i] < 'Q':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))