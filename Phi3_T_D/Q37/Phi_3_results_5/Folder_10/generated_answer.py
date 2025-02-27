def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 63 <= i <= 84 and 'E' <= char <= '~':
            continue
        else:
            result += char
    return result