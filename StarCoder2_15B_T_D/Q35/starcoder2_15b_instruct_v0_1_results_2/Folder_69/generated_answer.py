def remove_repeat_chars(s):
    count = {}
    for i, c in enumerate(s):
        if i in range(39, 43):
            count[c] = count.get(c, 0) + 1
    for c, num in count.items():
        if num > 1:
            s = s.replace(c, '')
    return s