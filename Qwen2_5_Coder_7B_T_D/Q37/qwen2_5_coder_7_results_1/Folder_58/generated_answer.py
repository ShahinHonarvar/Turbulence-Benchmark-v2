def filter_chars(s):
    to_remove = set()
    for i in range(503, 754):
        if '9' <= s[i] <= 'w':
            to_remove.add(s[i])
    return ''.join((ch for ch in s if ch not in to_remove))