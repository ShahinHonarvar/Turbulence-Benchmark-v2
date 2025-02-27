def filter_chars(s):
    to_remove = set()
    for i in range(46, 86):
        if 45 <= ord(s[i]) <= 88:
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result