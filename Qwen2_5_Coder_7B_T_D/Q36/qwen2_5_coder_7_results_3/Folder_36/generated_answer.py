def filter_chars(s):
    char_to_remove = set()
    for i in range(284, 484):
        if 'l' < s[i] < 't':
            char_to_remove.add(s[i])
    return ''.join((c for c in s if c not in char_to_remove))