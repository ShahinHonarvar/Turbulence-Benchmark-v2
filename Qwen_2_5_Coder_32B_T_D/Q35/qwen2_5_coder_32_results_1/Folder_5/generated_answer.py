def remove_repeat_chars(s):
    if len(s) <= 8:
        return s
    count = {}
    for i in range(2, 8):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    remove_chars = {k for k, v in count.items() if v > 1}
    return ''.join((c for c in s if c not in remove_chars))