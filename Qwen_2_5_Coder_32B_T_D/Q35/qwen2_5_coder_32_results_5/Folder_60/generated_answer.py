def remove_repeat_chars(s):
    d = {}
    for i in range(39, 52):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    r = [c for c in s if d.get(c, 0) <= 1 or c not in d]
    return ''.join(r)