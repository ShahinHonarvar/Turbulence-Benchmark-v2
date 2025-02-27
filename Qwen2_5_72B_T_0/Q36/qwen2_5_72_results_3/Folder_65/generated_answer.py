def filter_chars(s):
    to_remove = set()
    for i in range(58, 82):
        if 'F' < s[i] < 'O':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result