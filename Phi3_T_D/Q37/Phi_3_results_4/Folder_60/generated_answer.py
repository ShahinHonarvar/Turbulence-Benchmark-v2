def filter_chars(s):
    result = []
    for idx, char in enumerate(s):
        if 12 <= idx <= 77 and ':' <= char <= 'L':
            continue
        result.append(char)
    return ''.join(result)