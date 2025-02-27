def remove_repeat_chars(s):
    a = set()
    b = set()
    for i in range(14, 91):
        if s[i] not in a:
            a.add(s[i])
        else:
            b.add(s[i])
    return ''.join((c for c in s if c not in b))