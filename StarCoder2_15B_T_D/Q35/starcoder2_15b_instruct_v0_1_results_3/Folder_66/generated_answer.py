def remove_repeat_chars(string):
    count = {}
    for c in string[11:76]:
        count[c] = count.get(c, 0) + 1
    for c in count:
        if count[c] > 1:
            string = string.replace(c, '')
    return string