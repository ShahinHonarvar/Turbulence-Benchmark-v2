def filter_chars(s):
    to_remove = set()
    for i in range(63, 85):
        if 'E' <= s[i] <= '~':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result