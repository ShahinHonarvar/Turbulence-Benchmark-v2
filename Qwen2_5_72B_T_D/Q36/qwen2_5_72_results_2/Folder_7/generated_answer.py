def filter_chars(s):
    to_remove = set()
    for i in range(502, 946):
        if 'W' < s[i] < 'y':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))