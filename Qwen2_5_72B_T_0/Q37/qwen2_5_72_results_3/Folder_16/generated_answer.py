def filter_chars(s):
    to_remove = set()
    for i in range(225, 382):
        if 'D' <= s[i] <= 'Y':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result