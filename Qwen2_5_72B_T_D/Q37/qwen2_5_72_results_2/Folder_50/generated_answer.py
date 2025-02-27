def filter_chars(s):
    to_remove = set()
    for i in range(71, 97):
        if 'a' <= s[i] <= 'o':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result