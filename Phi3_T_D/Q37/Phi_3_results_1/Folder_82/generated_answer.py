def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 12 <= i <= 25 and 'P' <= char <= 'x':
            continue
        result.append(char)
    return ''.join(result)