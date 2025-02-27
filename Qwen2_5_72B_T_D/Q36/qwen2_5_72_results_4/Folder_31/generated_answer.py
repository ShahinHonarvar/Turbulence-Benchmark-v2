def filter_chars(s):
    to_remove = set()
    for i in range(14, 75):
        if 58 > ord(s[i]) > 75:
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result