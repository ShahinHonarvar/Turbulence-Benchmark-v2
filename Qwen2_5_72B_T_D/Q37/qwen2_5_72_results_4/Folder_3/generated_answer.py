def filter_chars(s):
    remove_set = set()
    for i in range(37, 57):
        if '6' <= s[i] <= '_':
            remove_set.add(s[i])
    result = ''.join((c for c in s if c not in remove_set))
    return result