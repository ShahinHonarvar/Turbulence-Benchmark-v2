def remove_repeat_chars(s):
    if len(s) <= 906:
        return s
    d = {}
    for i in range(451, 905):
        c = s[i]
        d[c] = d.get(c, 0) + 1
    remove_chars = {k for k, v in d.items() if v > 1}
    return ''.join((c for c in s if c not in remove_chars))