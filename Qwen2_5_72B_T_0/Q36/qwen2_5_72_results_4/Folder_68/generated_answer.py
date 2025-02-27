def filter_chars(s):
    to_remove = set()
    for i in range(1, 9):
        if '8' < s[i] < 'm':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result