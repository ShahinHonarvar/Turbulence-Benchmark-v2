def filter_chars(s):
    start, end = (36, 79)
    result = ''
    for i, char in enumerate(s):
        if start <= i <= end and 'a' <= char <= 'i':
            continue
        result += char
    return result