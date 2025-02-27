def filter_chars(s):
    to_remove = set()
    for i in range(44, 48):
        if '+' < s[i] < 'l':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result