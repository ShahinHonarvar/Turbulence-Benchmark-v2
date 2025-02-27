def remove_repeat_chars(s):
    seen = {}
    result = []
    unique = False
    for i, c in enumerate(s[35:63], start=35):
        if c in seen:
            seen[c] += 1
        else:
            seen[c] = 1
    for i, c in enumerate(s[35:63], start=35):
        if seen[c] == 1:
            result.append(c)
            unique = True
        if unique and seen[c] > 1:
            continue
        result.append(s[i])
    return ''.join(result)