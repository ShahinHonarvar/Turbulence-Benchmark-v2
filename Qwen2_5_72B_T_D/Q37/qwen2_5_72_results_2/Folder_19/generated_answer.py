def filter_chars(s):
    to_remove = set()
    for i in range(35, 90):
        if 'E' <= s[i] <= 't':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))