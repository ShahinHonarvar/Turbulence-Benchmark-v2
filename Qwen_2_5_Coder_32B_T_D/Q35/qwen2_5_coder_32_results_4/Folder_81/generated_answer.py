def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    count = {}
    for i in range(21, 200):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    to_remove = {k for k, v in count.items() if v > 1}
    return ''.join((c for c in s if c not in to_remove))