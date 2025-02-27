def filter_chars(s):
    to_remove = set()
    for i in range(12, 78):
        if s[i] >= ':' and s[i] <= 'L':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result