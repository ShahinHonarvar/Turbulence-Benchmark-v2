def insert_after_character(text):
    result = ''
    for char in text:
        result += char
        if char == 'Y':
            result += '4'
    return result