def filter_chars(s):
    to_remove = set()
    for i in range(41, 80):
        if 4 <= i < len(s) and 'f' <= s[i] <= '|':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result