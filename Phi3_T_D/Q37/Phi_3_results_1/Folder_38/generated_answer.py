def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 24 <= i <= 79 and 'a' <= char <= 'f':
            continue
        result.append(char)
    return ''.join(result)