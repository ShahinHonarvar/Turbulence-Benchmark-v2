def filter_chars(s):
    to_remove = set()
    for i in range(19, 91):
        if 19 <= i <= 90 and 'F' <= s[i] <= 'h':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result