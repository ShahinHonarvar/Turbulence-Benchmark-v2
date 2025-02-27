def remove_repeat_chars(s):
    s = list(s)
    for i in range(49, 74):
        c = s[i]
        if s.count(c) > 1:
            s = [x for x in s if x != c]
    return ''.join(s)