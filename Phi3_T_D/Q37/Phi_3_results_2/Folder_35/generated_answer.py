def filter_chars(s):
    for i in range(155, 404):
        char = s[i]
        if char >= '(' and char <= ']':
            s = s.replace(char, '')
    return s