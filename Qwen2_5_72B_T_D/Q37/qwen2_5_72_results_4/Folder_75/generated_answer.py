def filter_chars(s):
    to_remove = set()
    for i in range(34, 68):
        if 32 <= i < len(s) and 'W' <= s[i] <= 'x':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result