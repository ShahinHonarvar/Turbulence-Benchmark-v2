def filter_chars(s):
    to_remove = set()
    for i in range(42, 67):
        if '6' < s[i] < 'g':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result