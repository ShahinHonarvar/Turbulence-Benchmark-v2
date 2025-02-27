def filter_chars(s):
    to_remove = set()
    for i in range(19, 23):
        if ']' <= s[i] <= 't':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result