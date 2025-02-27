def remove_repeat_chars(s):
    d = {}
    for i in range(11, 79):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    return ''.join((c for c in s if c not in [k for k, v in d.items() if v > 1]))