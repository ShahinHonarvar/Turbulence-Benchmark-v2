def filter_chars(s):
    result = ''
    range_inclusive = range(38, 82)
    for i in range_inclusive:
        char = s[i]
        if '.' <= char < '^':
            result += char
    return result