def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 36 <= i <= 79 and '2' <= char <= 's':
            continue
        result += char
    return result