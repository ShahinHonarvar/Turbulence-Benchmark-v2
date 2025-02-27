def insert_after_character(text):
    result = ''
    for char in text:
        result += char
        if char == 'r':
            result += '1'
    return result