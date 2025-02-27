def filter_chars(s):
    to_remove = set()
    for i in range(71, 97):
        if 'a' <= s[i] <= 'o' or '_' <= s[i] <= 'o':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))