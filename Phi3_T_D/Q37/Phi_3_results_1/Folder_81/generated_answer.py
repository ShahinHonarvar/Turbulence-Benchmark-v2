def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 19 <= i <= 92:
            if '8' <= char <= 'm':
                continue
        result.append(char)
    return ''.join(result)