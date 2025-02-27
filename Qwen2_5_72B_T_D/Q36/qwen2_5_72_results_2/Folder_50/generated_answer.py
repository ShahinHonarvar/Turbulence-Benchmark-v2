def filter_chars(s):
    to_remove = set()
    for i in range(61, 88):
        if '%' < s[i] < 'q':
            to_remove.add(s[i])
    result = ''.join([c for c in s if c not in to_remove])
    return result