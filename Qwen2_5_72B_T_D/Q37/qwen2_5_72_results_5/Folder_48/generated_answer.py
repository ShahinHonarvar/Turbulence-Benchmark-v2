def filter_chars(s):
    to_remove = set()
    for i in range(513, 878):
        if 63 <= ord(s[i]) <= 110:
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))