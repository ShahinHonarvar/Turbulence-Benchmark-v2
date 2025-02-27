def filter_chars(s):
    to_remove = set()
    for i in range(331, 713):
        if 'M' < s[i] < '_':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))