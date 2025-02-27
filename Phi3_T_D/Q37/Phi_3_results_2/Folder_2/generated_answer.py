def filter_chars(s):
    result = ''
    for char in s[477:985]:
        if ',' <= char <= 'V':
            continue
        result += char
    return result + s[985:]