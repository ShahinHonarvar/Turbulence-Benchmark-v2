def filter_chars(s):
    to_remove = set()
    for i in range(55, 66):
        if 5 < ord(s[i]) < 124:
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))