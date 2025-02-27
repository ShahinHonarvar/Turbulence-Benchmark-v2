def filter_chars(s):
    to_remove = set()
    for i in range(31, 39):
        if 59 <= ord(s[i]) <= 103:
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))