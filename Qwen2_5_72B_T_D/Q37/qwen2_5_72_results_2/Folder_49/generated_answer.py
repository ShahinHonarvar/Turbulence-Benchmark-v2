def filter_chars(s):
    to_remove = set()
    for i in range(42, 98):
        if s[i] >= '*' and s[i] <= 'b':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result