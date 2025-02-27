def filter_chars(s):
    to_remove = set()
    for i in range(29, 98):
        if 'a' <= s[i] <= 'n' or s[i] == '-':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result