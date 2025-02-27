def filter_chars(s):
    to_remove = set()
    for i in range(138, 921):
        if 138 <= i <= 920 and '6' <= s[i] <= 'A':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result