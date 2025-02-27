def remove_repeat_chars(s):
    d = {}
    for i in range(1, 5):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    r = [c for c in s if c not in d or d[c] == 1]
    return ''.join(r)