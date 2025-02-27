def filter_chars(s):
    to_remove = set()
    for i in range(343, 665):
        if '%' < s[i] < 'U':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result