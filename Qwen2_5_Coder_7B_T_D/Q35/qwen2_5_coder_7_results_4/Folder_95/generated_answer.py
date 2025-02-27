def remove_repeat_chars(s):
    count = {}
    for i, c in enumerate(s):
        if 32 < i < 99:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
    result = []
    for i, c in enumerate(s):
        if 32 < i < 99 and count[c] == 1 or (32 >= i or i >= 99):
            result.append(c)
    return ''.join(result)