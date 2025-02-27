def filter_chars(s):
    result = list(s)
    for i in range(35, 99):
        if 'A' <= result[i] <= 'b':
            result[i] = ''
    return ''.join(result)