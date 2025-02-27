def filter_chars(s):
    to_remove = set()
    for i in range(20, 63):
        if 'i' <= s[i] <= 'k':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result