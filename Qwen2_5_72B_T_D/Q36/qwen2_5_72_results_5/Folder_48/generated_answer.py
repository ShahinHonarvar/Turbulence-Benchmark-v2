def filter_chars(s):
    to_remove = set()
    for i in range(154, 222):
        if 'A' < s[i] < 'f':
            to_remove.add(s[i])
    result = ''.join([c for c in s if c not in to_remove])
    return result