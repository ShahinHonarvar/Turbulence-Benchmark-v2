def remove_repeat_chars(s):
    d = {}
    for i in range(101, 200):
        if i < len(s):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
    chars_to_remove = {k for k, v in d.items() if v > 1}
    return ''.join((c for c in s if c not in chars_to_remove))