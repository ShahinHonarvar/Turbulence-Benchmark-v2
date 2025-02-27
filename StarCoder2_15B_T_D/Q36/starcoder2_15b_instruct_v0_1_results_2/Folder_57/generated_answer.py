def filter_chars(text):
    result = ''
    for i, c in enumerate(text):
        if i < 70 or i >= 74 or c <= 'A' or (c >= 'U'):
            result += c
    return result