def remove_repeat_chars(s):
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in count:
        if count[c] > 1 and s.index(c) >= 0 and (s.index(c) < 5):
            s = ''.join(s.split(c))
    return s