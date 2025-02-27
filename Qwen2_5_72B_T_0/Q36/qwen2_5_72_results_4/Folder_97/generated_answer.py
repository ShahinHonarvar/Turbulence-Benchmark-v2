def filter_chars(s):
    to_remove = set()
    for i in range(309, 591):
        if 309 <= i < len(s) and s[i] > 'S' and (s[i] < 'm'):
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result