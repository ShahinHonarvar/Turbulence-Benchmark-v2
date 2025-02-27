def filter_chars(s):
    if len(s) < 526:
        return s
    to_remove = set()
    for i in range(323, 526):
        if ')' < s[i] < 'O':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))