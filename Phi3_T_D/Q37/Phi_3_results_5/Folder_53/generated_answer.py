def filter_chars(s):
    result = []
    for index, char in enumerate(s):
        if 83 <= index <= 99 and '*' <= char <= 'j':
            continue
        result.append(char)
    return ''.join(result)