def filter_chars(s):
    to_remove = set()
    for i in range(227, 236):
        if 'D' <= s[i] <= 'u':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result