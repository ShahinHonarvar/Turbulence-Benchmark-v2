def remove_repeat_chars(s):
    seen = set(s[49:74])
    count = {}
    for c in s[49:74]:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    for c in seen:
        if count[c] > 1:
            s = s.replace(c, '')
    return s