def filter_chars(s):
    to_remove = set()
    for i in range(75, 100):
        if 75 <= i < len(s) and '8' <= s[i] <= 'e':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result