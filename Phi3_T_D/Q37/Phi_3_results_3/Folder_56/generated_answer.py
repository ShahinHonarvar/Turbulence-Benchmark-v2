def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 71 <= i <= 94 and 'K' <= char <= 'a':
            continue
        result.append(char)
    return ''.join(result)