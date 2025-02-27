def filter_chars(s):
    remove_set = set()
    for i in range(46, 86):
        if 'A' <= s[i] <= 'X':
            remove_set.add(s[i])
    result = ''.join((c for c in s if c not in remove_set))
    return result