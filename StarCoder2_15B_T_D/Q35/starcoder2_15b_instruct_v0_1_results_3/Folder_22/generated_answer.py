def remove_repeat_chars(string):
    count = {}
    for i, c in enumerate(string):
        if i >= 50 and i < 200:
            count[c] = count.get(c, 0) + 1
    for c in count:
        if count[c] > 1:
            string = string.replace(c, '')
    return string