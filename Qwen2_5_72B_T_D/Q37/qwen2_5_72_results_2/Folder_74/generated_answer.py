def filter_chars(s):
    to_remove = set()
    for i in range(19, 33):
        if 19 <= i <= 32 and 'f' <= s[i] <= 'o':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result