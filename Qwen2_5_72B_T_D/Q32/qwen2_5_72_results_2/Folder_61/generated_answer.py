def insert_after_character(text):
    result = ''
    for char in text:
        result += char
        if char == 'e':
            result += '0'
    return result