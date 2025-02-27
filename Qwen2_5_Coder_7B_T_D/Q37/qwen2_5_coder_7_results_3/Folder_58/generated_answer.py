def filter_chars(s):
    filtered_chars = set()
    for i in range(503, 754):
        char = s[i]
        if '9' <= char <= 'w':
            filtered_chars.add(char)
    result = []
    for char in s:
        if char not in filtered_chars:
            result.append(char)
    return ''.join(result)