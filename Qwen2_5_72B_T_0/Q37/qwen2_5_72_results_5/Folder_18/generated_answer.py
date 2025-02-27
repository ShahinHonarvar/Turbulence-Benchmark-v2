def filter_chars(s):
    to_remove = set()
    for i in range(770, 971):
        if 0 <= i < len(s) and '-' <= s[i] <= 'D':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result