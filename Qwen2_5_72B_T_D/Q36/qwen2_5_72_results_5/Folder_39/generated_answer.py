def filter_chars(s):
    to_remove = set()
    for i in range(43, 59):
        if '5' < s[i] < 'C':
            to_remove.add(s[i])
    result = ''.join([c for c in s if c not in to_remove])
    return result