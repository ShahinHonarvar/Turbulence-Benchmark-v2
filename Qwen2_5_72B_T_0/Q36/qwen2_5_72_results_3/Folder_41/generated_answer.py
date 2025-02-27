def filter_chars(s):
    to_remove = set()
    for i in range(81, 89):
        if 'f' < s[i] < '{':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result