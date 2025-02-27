def filter_chars(s):
    to_remove = set()
    for i in range(25, 98):
        if 0 <= i < len(s) and 'm' <= s[i] <= 'w':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))