def remove_repeat_chars(s):
    d = {}
    for i in range(21, 35):
        c = s[i]
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    r = set((c for c in d if d[c] > 1))
    return ''.join((c for c in s if c not in r))