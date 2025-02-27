def remove_repeat_chars(string):
    counts = {}
    result = []
    for c in string:
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1
        if counts[c] == 1:
            result.append(c)
    return ''.join(result)