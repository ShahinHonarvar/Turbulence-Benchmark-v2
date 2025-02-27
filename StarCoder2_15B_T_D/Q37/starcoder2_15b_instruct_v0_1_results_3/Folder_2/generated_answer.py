def filter_chars(text):
    result = ''
    for char in text:
        if not (477 <= ord(char) <= 984 and ',' <= char <= 'V'):
            result += char
    return result