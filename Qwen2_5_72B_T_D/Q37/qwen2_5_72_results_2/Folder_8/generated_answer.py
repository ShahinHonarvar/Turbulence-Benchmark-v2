def filter_chars(s):
    to_remove = set()
    for i in range(41, 87):
        if 41 <= i <= 86 and 'S' <= s[i] <= 's':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result