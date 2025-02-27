def remove_repeat_chars(s):
    occurrences = {}
    result = []
    for i, c in enumerate(s):
        if i >= 20 and i < 43:
            occurrences[c] = occurrences.get(c, 0) + 1
            if occurrences[c] == 1:
                result.append(c)
    return ''.join(result)