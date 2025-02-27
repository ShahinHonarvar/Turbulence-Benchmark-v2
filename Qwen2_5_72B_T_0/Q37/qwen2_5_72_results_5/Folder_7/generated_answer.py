def filter_chars(s):
    to_remove = set()
    for i in range(521, 723):
        if i < len(s) and '>' <= s[i] <= '_':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result