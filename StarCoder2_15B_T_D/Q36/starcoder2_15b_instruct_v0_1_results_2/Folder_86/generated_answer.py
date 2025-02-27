def filter_chars(text):
    result = ''
    for char in text:
        if char <= 'X' or char >= '}':
            result += char
    return result