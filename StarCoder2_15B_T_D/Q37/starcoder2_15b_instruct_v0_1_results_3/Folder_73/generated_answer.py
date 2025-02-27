def filter_chars(text):
    result = ''
    for i, char in enumerate(text):
        if not (22 <= i <= 85 and '7' <= char <= 'e'):
            result += char
    return result