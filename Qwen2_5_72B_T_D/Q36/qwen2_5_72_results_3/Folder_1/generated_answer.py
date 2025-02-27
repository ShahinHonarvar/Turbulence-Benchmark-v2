def filter_chars(s):
    to_remove = set()
    for i in range(69, 87):
        if 35 < ord(s[i]) < 76:
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result