def filter_chars(s):
    to_remove = set()
    for i in range(29, 80):
        if 29 <= i <= 79 and 'K' <= s[i] <= 'z':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result