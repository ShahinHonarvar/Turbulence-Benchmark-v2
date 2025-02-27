def remove_repeat_chars(string):
    result = ''
    counts = {}
    for c in string:
        counts[c] = counts.get(c, 0) + 1
    for i, c in enumerate(string):
        if counts[c] > 1 and 10 <= i < 100:
            continue
        result += c
    return result