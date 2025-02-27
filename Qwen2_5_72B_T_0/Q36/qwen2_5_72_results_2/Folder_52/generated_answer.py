def filter_chars(s):
    to_remove = set()
    for i in range(49, 56):
        if 'I' < s[i] < 'a':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result