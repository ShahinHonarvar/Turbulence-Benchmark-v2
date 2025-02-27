def filter_chars(s):
    s = list(s)
    to_remove = set()
    for i in range(503, 754):
        char = s[i]
        if '9' <= char <= 'w':
            to_remove.add(char)
    return ''.join((c for c in s if c not in to_remove))