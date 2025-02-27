def filter_chars(s):
    to_remove = set()
    for i in range(669, 888):
        if 66 <= ord(s[i]) <= 89:
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result