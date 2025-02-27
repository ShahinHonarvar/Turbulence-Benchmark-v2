def filter_chars(s):
    to_remove = set()
    for i in range(43, 81):
        if 44 <= i <= len(s) and '=' <= s[i - 1] <= 'E':
            to_remove.add(s[i - 1])
    result = ''.join((c for c in s if c not in to_remove))
    return result