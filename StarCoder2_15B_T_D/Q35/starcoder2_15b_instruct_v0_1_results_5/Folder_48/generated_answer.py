def remove_repeat_chars(string):
    count = {}
    for c in string:
        count[c] = count.get(c, 0) + 1
    for c in count:
        if count[c] > 1 and 409 < string.index(c) < 502:
            string = string.replace(c, '')
    return string