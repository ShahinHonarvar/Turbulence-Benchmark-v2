def remove_repeat_chars(s):
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c, freq in count.items():
        if freq > 1:
            s = s.replace(c, '')
    return s