def filter_chars(s):
    to_remove = set()
    for i in range(379, 900):
        if 379 <= i <= 898 and 'M' <= s[i] <= 'v':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result