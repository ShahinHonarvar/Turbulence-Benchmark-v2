def filter_chars(s):
    result = ''
    for i, char in enumerate(s[27:66]):
        if 'O' <= char <= 'd':
            continue
        result += s[i]
    return result