def remove_repeat_chars(s):
    lookup = {}
    for i in range(6, 9):
        if s[i] in lookup:
            lookup[s[i]] += 1
        else:
            lookup[s[i]] = 1
    return ''.join([c for i, c in enumerate(s) if i < 6 or i > 8 or lookup[c] == 1])