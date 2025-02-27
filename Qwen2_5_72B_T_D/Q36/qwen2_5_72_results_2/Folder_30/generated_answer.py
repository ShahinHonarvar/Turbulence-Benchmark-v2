def filter_chars(s):
    to_remove = set()
    for i in range(23, 45):
        if 23 <= i < len(s) and '3' < s[i] < 'I':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result