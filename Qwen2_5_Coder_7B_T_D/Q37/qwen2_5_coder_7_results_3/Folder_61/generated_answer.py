def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if (i == 5 or i == 6) and 'G' <= char <= 'p':
            continue
        result.append(char)
    return ''.join(result)