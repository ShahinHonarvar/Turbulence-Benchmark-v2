def filter_chars(s):
    to_remove = set()
    for i in range(19, 93):
        if 19 <= i <= 92 and '8' <= s[i] <= 'm':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result