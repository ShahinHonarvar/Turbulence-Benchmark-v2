def remove_repeat_chars(s):
    if len(s) <= 36:
        return s
    count = {}
    for i in range(21, 36):
        if s[i] not in count:
            count[s[i]] = 1
        else:
            count[s[i]] += 1
    remove_set = {k for k, v in count.items() if v > 1}
    return ''.join((c for c in s if c not in remove_set))