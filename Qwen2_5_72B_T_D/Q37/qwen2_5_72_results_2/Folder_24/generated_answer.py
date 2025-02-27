def filter_chars(s):
    to_remove = set()
    for i in range(36, 80):
        if '2' <= s[i] <= 's':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result