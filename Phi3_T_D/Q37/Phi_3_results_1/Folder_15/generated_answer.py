def filter_chars(s):
    result = ''
    for i in range(2, 7):
        char = s[i]
        if '?' <= char <= 'f':
            continue
        result += char
    for i in range(7, len(s)):
        char = s[i]
        if '?' <= char <= 'f':
            continue
        result += char
    return result