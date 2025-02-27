def filter_chars(s):
    to_remove = set()
    for i in range(35, 99):
        if 'A' <= s[i] <= 'b':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))