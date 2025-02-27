def filter_chars(s):
    to_remove = set()
    for i in range(171, 636):
        if 'c' < s[i] < 's':
            to_remove.add(s[i])
    result = ''.join((ch for ch in s if ch not in to_remove))
    return result