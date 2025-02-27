def filter_chars(s):
    to_remove = set()
    for i in range(503, 754):
        if 57 <= ord(s[i]) <= 119:
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result