def filter_chars(s):
    filter_set = set(s[5:7])
    result = []
    for char in s:
        if char not in filter_set or not 'G' <= char <= 'p':
            result.append(char)
    return ''.join(result)