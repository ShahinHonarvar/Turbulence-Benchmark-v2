def remove_repeat_chars(s):
    count = {}
    for i, c in enumerate(s):
        if 25 < i < 80:
            count[c] = count.get(c, 0) + 1
    for c in count:
        if count[c] > 1:
            s = s.replace(c, '')
    return s