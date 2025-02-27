def filter_chars(s):
    to_remove = set()
    for i in range(43, 81):
        if 4 <= ord(s[i]) - ord('A') <= 14:
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result