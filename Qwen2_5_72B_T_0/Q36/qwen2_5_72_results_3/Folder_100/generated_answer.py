def filter_chars(s):
    to_remove = set()
    for i in range(43, 69):
        if 'B' < s[i] < 'r':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result