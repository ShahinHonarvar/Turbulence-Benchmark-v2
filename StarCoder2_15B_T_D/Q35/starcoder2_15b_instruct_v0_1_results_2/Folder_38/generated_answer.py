def remove_repeat_chars(s):
    count = {}
    for c in s[36:85]:
        count[c] = count.get(c, 0) + 1
    for c in count:
        if count[c] > 1:
            s = s.replace(c, '')
    return s