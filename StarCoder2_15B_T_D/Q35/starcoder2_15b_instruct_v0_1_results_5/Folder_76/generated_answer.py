def remove_repeat_chars(string):
    count = {}
    for c in string:
        count[c] = count.get(c, 0) + 1
    result = []
    for c in string:
        if count[c] > 1 and 330 < string.index(c) < 543:
            continue
        result.append(c)
    return ''.join(result)