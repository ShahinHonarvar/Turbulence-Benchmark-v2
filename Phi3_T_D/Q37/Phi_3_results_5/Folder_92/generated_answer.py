def filter_chars(s):
    result = []
    for i, c in enumerate(s):
        if i < 4 or not '7' <= c <= 'o' or c in s[4:4 + 1]:
            continue
        result.append(c)
    return ''.join(result)