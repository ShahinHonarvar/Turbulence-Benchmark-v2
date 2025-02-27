def filter_chars(s):
    to_remove = set()
    for i in range(10, 80):
        if 63 < ord(s[i]) < 109:
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))