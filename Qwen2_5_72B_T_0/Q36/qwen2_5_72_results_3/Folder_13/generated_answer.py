def filter_chars(s):
    to_remove = set()
    for i in range(323, 526):
        if 41 < ord(s[i]) < 79:
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result